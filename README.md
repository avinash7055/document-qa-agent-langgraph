# Document QA Agent with LangGraph

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub repo size](https://img.shields.io/github/repo-size/avinash7055/document-qa-agent-langgraph)

A powerful AI-driven tool that processes Excel documents and answers user questions using LangGraph for workflow orchestration, LangChain with Grok for natural language understanding, and Streamlit for a user-friendly interface.

## Project Description

The **Document QA Agent** is a sophisticated application designed to extract actionable insights from Excel files (.xlsx). It combines state-of-the-art AI technologies with a streamlined workflow to enable users to upload documents, ask questions, and receive precise answers. The project leverages LangGraph to manage a two-step process—document processing and question answering—while integrating the Grok model from xAI for advanced question-answering capabilities. A Streamlit-based UI makes it accessible to non-technical users.

### Key Features
- **Excel Support:** Processes `.xlsx` files, extracting content from all sheets using `pandas`.
- **AI Question Answering:** Employs Grok (`llama-3.1-8b-instant`) to provide context-aware answers based on document data.
- **Workflow Management:** Uses LangGraph to define a clear, modular pipeline for document handling and QA.
- **Web Interface:** Offers an intuitive Streamlit UI for file uploads, question input, and answer display.
- **Robustness:** Includes error handling for file processing and API interactions.

### Use Cases
- Extract totals or summaries from financial spreadsheets.
- Query specific data points from tabular datasets.
- Analyze structured data in Excel for quick insights.

### Technical Stack
- **LangGraph:** Orchestrates the processing and QA workflow.
- **LangChain & Grok:** Powers the NLP engine for question interpretation and response generation.
- **Pandas:** Parses Excel files into text for processing.
- **Streamlit:** Provides a web-based front-end for user interaction.



## Prerequisites
- **Python:** Version 3.8 or higher
- **Git:** For cloning and version control
- **GitHub Account:** For repository access
- **Grok API Key:** Required for `langchain-groq`, obtainable from [xAI](https://xai.com)

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/avinash7055/document-qa-agent-langgraph.git
cd document-qa-agent-langgraph

Make virtual environment
python -m venv venv
venv\Scripts\Activate

pip install -r requirements.txt

streamlit run app.py
