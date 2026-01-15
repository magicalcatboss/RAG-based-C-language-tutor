# RAG-based C language Tutor

An intelligent C programming tutor powered by Retrieval-Augmented Generation (RAG). It leverages high-quality standard documentation from CppReference and Google's Gemini API to provide accurate and reliable answers for C learners.

## Core Architecture (4-Step Workflow)

1.  **Vector Store**: High-efficiency local retrieval using `ChromaDB` and `sentence-transformers`.
2.  **Data Acquisition**: Extracting high-quality standard documentation from `CppReference`.
3.  **Generation Engine**: Integration with `Google Gemini API` as the core reasoning brain.
4.  **Web Service**: Backend API built with `FastAPI`.

## Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Environment Configuration
Create a `.env` file in the root directory and add:
```env
GEMINI_API_KEY=your_api_key_here
```

### 3. Run the Service
```bash
uvicorn main:app --reload
```

## Tech Stack
- **LLM**: Google Gemini
- **Embedding**: all-MiniLM-L6-v2
- **Vector DB**: ChromaDB
- **Backend**: FastAPI
- **Scraper**: BeautifulSoup4
