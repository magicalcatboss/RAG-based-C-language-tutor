# Project Plan & Todo List

## Phase 1: Project Initialization & Setup
- [ ] Create project directory and detailed folder structure
- [ ] Initialize Git repository
- [ ] Create `README.md` with project description
- [ ] Create `PROJECT_PLAN.md` with detailed todo list

## Phase 2: Knowledge Base & RAG Pipeline
- [ ] Define data sources (C Programming Standards - MISRA, CERT C, etc.)
- [ ] Design data ingestion scripts (Python)
    - [ ] PDF/Markdown text extraction
    - [ ] Text chunking and cleaning
- [ ] Set up Vector Database (e.g., ChromaDB or FAISS)
- [ ] Implement Embedding generation (using HuggingFace or OpenAI embeddings)
- [ ] Develop Retrieval System (Query processing and similarity search)

## Phase 3: Backend API (Python/FastAPI)
- [ ] Setup Python virtual environment and `requirements.txt`
- [ ] Initialize FastAPI application
- [ ] Create RAG Management Endpoints (Ingest, Clear DB)
- [ ] Create Chat Endpoint (Similarity search + LLM Context Injection)
- [ ] Implement System Prompt specialized for C Language Standards

## Phase 4: Frontend Application (React/Vite)
- [ ] Initialize React Project with Vite (TypeScript recommended)
- [ ] Setup UI Components (TailwindCSS)
    - [ ] Chat Window
    - [ ] Message Input
    - [ ] Source/Reference Display
- [ ] Integrate API with Frontend
- [ ] Polish UI/UX (Markdown rendering for code blocks)

## Phase 5: Testing & Deployment
- [ ] Verify answers against specific C standards
- [ ] Dockerize application (Dockerfile & docker-compose.yml)
- [ ] Write documentation for usage and contribution
