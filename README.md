# Sustainable Technology: Balancing Innovation and Environmental Impact

## Project Overview

This project contains AI research workflows that explore topics in depth and deliver results in multiple languages. It features three main modules:

1. **Chain Workflow** - A sequential research process that plans, researches, synthesizes, and translates content
2. **Self-Reflection Workflow** - An enhanced workflow that includes critical self-assessment and iterative improvement
3. **AI Agent Basic RAG** - A module for extracting and processing data from PDF documents using OCR and RAG (Retrieval Augmented Generation)

## Setup

### Prerequisites

- Python 3.9 or higher
- OpenAI API key
- Mistral API key (for AI Agent Basic RAG module)

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```
3. Copy the `.env.example` file to `.env` and add your required API keys:
   ```bash
   cp .env.example .env
   ```
4. Edit the `.env` file and set your API keys:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   MISTRAL_API_KEY=your_mistral_api_key_here
   ```

## Running the Modules

### Chain Workflow

To run the basic chain workflow research process:

```bash
python -m modules.agentic-ai-workflows.chain-workflow.main
```

This will execute a research workflow on the topic "Sustainable Technology: Balancing Innovation and Environmental Impact" and generate a multilingual report.

### Self-Reflection Workflow

To run the enhanced workflow with self-reflection capabilities:

```bash
python -m modules.agentic-ai-workflows.self-reflection.main
```

This workflow includes additional steps for critical assessment and improvement of the research before finalizing.

### AI Agent Basic RAG

To run the PDF extraction and data processing module:

```bash
python -m modules.ai-agent-basic-rag.main
```

This module will:

1. Upload a PDF file (company.pdf) to Mistral for OCR processing
2. Extract key bullet points from the document
3. Store these points in ChromaDB
4. Save the extraction results to bullet_points.md

## Output

The research results will be saved as markdown files in the project root directory:

- Main research report in English: `Sustainable Technology: Balancing Innovation and Environmental Impact.md` and `Sustainable Technology: Balancing Innovation and Environmental Impact (Expanded Report).md`
- Translated versions: `translated_id.md` (Indonesian), `translated_ja.md` (Japanese), and `translated_ko.md` (Korean)
- PDF extraction results: `bullet_points.md`

## Customizing Research Topics

To change the research topic, modify the `topic` variable in the `main.py` file of either module.

## Database

The AI Agent Basic RAG module uses ChromaDB to store extracted data. The database is stored in the `data/` directory.
