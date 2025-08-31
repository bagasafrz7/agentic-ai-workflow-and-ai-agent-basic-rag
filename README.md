# Sustainable Technology: Balancing Innovation and Environmental Impact

## Project Overview

This project contains AI research workflows that explore topics in depth and deliver results in multiple languages. It features two main workflow types:

1. **Chain Workflow** - A sequential research process that plans, researches, synthesizes, and translates content
2. **Self-Reflection Workflow** - An enhanced workflow that includes critical self-assessment and iterative improvement

## Setup

### Prerequisites

- Python 3.9 or higher
- OpenAI API key

### Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -e .
   ```
3. Copy the `.env.example` file to `.env` and add your OpenAI API key:
   ```bash
   cp .env.example .env
   ```
4. Edit the `.env` file and set your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
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

## Output

The research results will be saved as markdown files in the project root directory:

- Main research report in English: `Sustainable Technology: Balancing Innovation and Environmental Impact.md`
- Translated versions: `translated_id.md` (Indonesian), `translated_ja.md` (Japanese), and `translated_ko.md` (Korean)

## Customizing Research Topics

To change the research topic, modify the `topic` variable in the `main.py` file of either module.
