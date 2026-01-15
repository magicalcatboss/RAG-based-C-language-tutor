# Project Plan: RAG-based C language Tutor

## Phase 1: Infrastructure & Meta Files
- [x] Git & GitHub Initialization
- [x] Project Meta Files (.gitignore, LICENSE)
- [ ] Dependency Management (requirements.txt)

## Phase 2: Core Development (User-Calibrated)

### Task 1: Vector Store & Embedding Module
- [ ] Install `FAISS` and `sentence-transformers`.
- [ ] Implement `VectorStore` class supporting document addition and similarity search.

### Task 2: CppReference Data Scraper
- [ ] Develop `crawl_cppreference` function for content extraction.
- [ ] Clean data and perform batch ingestion into the vector store.

### Task 3: Gemini API Integration
- [ ] Integrate `google-generativeai`.
- [ ] Design professional C Tutor system prompt template.

### Task 4: FastAPI Backend Integration
- [ ] Develop `main.py` to orchestrate retrieval and generation logic.
- [ ] Expose `/ask` endpoint.

## Phase 3: UI & Interaction
- [ ] Develop Streamlit chat interface.
- [ ] Implement Markdown rendering and code syntax highlighting.

## Phase 4: Testing & Deployment
- [ ] Verify retrieval accuracy and edge-case handling.
- [ ] Dockerize the application.
