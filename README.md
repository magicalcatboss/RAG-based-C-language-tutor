# 🎓 C-Language RAG Tutor

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.95.1+-05998b.svg)](https://fastapi.tiangolo.com/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.22.0+-FF4B4B.svg)](https://streamlit.io/)
[![Gemini API](https://img.shields.io/badge/Gemini-2.0%20Flash-blue)](https://ai.google.dev/)

An intelligent C language programming tutor powered by **Retrieval-Augmented Generation (RAG)**. This project combines high-quality documentation from **CppReference** with the reasoning power of **Google Gemini 2.0 Flash** to provide accurate, context-aware answers to your programming questions.

---

## ✨ Features

- **Context-Aware Answers**: Uses RAG to fetch relevant documentation snippets before generating answers.
- **Reference-Backed**: All answers are grounded in the CppReference standard library documentation.
- **Modern UI**: A clean, interactive chat interface built with Streamlit.
- **Scalable Backend**: FastAPI-powered backend with FAISS vector search for millisecond-latency retrieval.
- **Private & Control**: Only your API key is used, and everything runs locally.

---

## 🛠️ Architecture

1.  **Vector Store**: Uses `FAISS` for efficient semantic search of C language documentation.
2.  **Embeddings**: Powered by `sentence-transformers` for high-quality text representation.
3.  **LLM Engine**: Integration with `Gemini 2.0 Flash` for expert-level tutoring.
4.  **Frontend**: Interactive Streamlit dashboard with sidebar references.

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9 or higher
- A Google Gemini API Key (Get it at [Google AI Studio](https://aistudio.google.com/))

### 2. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/yourusername/RAG-based-C-language-Tutor.git
cd RAG-based-C-language-Tutor
pip install -r requirements.txt
```

### 3. Environment Configuration
Create a `.env` file in the root directory and add your Gemini API key:
```env
GEMINI_API_KEY=your_api_key_here
```

### 4. Running the Application

#### Option A: One-Click Startup (Windows)
Simply double-click the `start_tutor.bat` file. It will automatically:
1. Start the FastAPI backend on port `8899`.
2. Start the Streamlit frontend and open your browser.

#### Option B: Manual Startup
If you are on Linux/macOS or prefer the terminal, run the following in **two separate** terminals:

**Terminal 1 (Backend):**
```bash
python main.py
```

**Terminal 2 (Frontend):**
```bash
python -m streamlit run app.py
```

---

## 📂 Project Structure

- `app.py`: Streamlit frontend interface.
- `main.py`: FastAPI backend and API entry point.
- `vector_store.py`: Vector database management (FAISS).
- `gemini_engine.py`: Logic for Gemini API integration.
- `scraper.py`: Documentation scraper for fetching CppReference data.
- `ingest_data.py`: Tool to process scraped data into the vector store.
- `faiss_index.pkl`: Pre-computed vector index (included in repo).

---

## 🎯 Usage
- Ask questions like: *"How does a pointer work in C?"* or *"Explain the difference between malloc and calloc."*
- View the specific documentation snippets used by the AI in the sidebar.
- Use the code snippets provided by the tutor directly in your editor.

---

## 📄 License
This project is licensed under the MIT License - see the `LICENSE` file for details.

---

## 🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
