import os
import re
from mistralai import Mistral
from dotenv import load_dotenv
from openai import OpenAI
import chromadb
from chromadb.utils.embedding_functions import OpenAIEmbeddingFunction
from loguru import logger

load_dotenv()

# Init Clients
mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
openai_client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
chroma_client = chromadb.PersistentClient(path="data")
ef = OpenAIEmbeddingFunction(api_key=os.getenv("OPENAI_API_KEY"), model_name="text-embedding-3-small")

# Reset collection
try:
    chroma_client.delete_collection(name="companies_data")
except:
    pass
collection = chroma_client.create_collection(name="companies_data", embedding_function=ef)

# Upload & OCR
logger.info("Uploading file to S3")
uploaded_pdf = mistral_client.files.upload(
    file={
        "file_name": "company.pdf",
        "content": open("company.pdf", "rb"),
    },
    purpose="ocr"
)

signed_url = mistral_client.files.get_signed_url(file_id=uploaded_pdf.id)

logger.info("Processing OCR")
ocr_response = mistral_client.ocr.process(
    model="mistral-ocr-latest",
    document={
        "type": "document_url",
        "document_url": signed_url.url,
    },
)

pages = ocr_response.model_dump().get("pages")
bullet_points = ""

for page_num, page in enumerate(pages[:10], start=1):
    markdown = page.get("markdown")

    SYSTEM_PROMPT = """
        You are data extractor.
        You will need to extract bullet points from the markdown.

        OUTPUT FORMAT:
        - [point_1]
        - [point_2]
        - [point_3]

        IMPORTANT:
        - Flat Bullet Point, No nested bullet point.
        - Each bullet point should be short and to the point.
        - Do not add any headings
        - Do not add any explanations
        - Always include the Numbers and Date if present in the markdown.
    """

    logger.info(f"Extracting bullet points: {page_num}")
    response = openai_client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": f"Convert the following markdown to bullet points: {markdown}"}
        ]
    )
    result = response.choices[0].message.content
    bullet_points += result + "\n\n"

    bullets = [
        re.sub(r"^[\-\•\–\●\s]+", "", bp).strip()  # hapus simbol bullet + spasi
        for bp in result.split("\n")
        if bp.strip()
    ]

    bullets = [bp.encode("utf-8", "ignore").decode("utf-8") for bp in bullets]

    logger.info(f"[DEBUG] Page {page_num} | bullets: {len(bullets)}")

    # Insert ke Chroma per bullet
    for i, doc in enumerate(bullets):
        try:
            collection.add(
                documents=[doc],
                metadatas=[{"page": page_num}],
                ids=[f"page_{page_num}_{i}"]
            )
        except Exception as e:
            logger.error(f"❌ Skip bullet {i} on page {page_num}: {e}")

# Save ke file markdown
with open("bullet_points.md", "w") as f:
    f.write(bullet_points)

logger.info("✅ All bullet points stored into ChromaDB")
