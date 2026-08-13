# EnterpriseRAG

A Retrieval-Augmented Generation (RAG) backend for querying your own documents in natural language. Upload a PDF, ask questions about it, and get grounded answers with source citations — built as a modular service layer (ingestion, vector retrieval, RAG orchestration) rather than a single script, with support for two interchangeable vector store backends.

## What it does

- **Ingests documents** — parses and chunks PDFs (via PyMuPDF) and stores them as embeddings for retrieval
- **Retrieves relevant context** — semantic search over the document store using sentence-transformer embeddings, returning ranked passages with metadata
- **Answers questions** — a RAG pipeline that grounds LLM responses (Gemini / OpenAI, via LangChain) in the retrieved context rather than the model's raw knowledge
- **Supports two vector store backends** — ChromaDB (local, file-based) and Qdrant (containerized, production-style), so retrieval quality/behavior can be compared across stores
- **Ships as a FastAPI service** — packaged with a Dockerfile and docker-compose so the API and the Qdrant vector store can be run as containers

## Architecture

```
                 ┌──────────────┐
   PDF file  ──▶ │  Ingestion   │  chunk + embed
                 │  Service     │
                 └──────┬───────┘
                        ▼
              ┌───────────────────┐
              │   Vector Store     │  ChromaDB (local)
              │  (Chroma / Qdrant) │  or Qdrant (Docker)
              └─────────┬──────────┘
                        ▼
                 ┌──────────────┐
   query    ──▶  │  Retrieval   │  semantic search,
                 │  Service     │  top-k passages
                 └──────┬───────┘
                        ▼
                 ┌──────────────┐
                 │  RAG Service │  LLM (Gemini/OpenAI)
                 │              │  grounded answer
                 └──────┬───────┘
                        ▼
                    Answer + sources
```

## Tech stack

- **Orchestration:** LangChain, LangGraph
- **LLMs:** Google Gemini, OpenAI (swappable)
- **Embeddings:** sentence-transformers
- **Vector stores:** ChromaDB, Qdrant
- **Document parsing:** PyMuPDF
- **API:** FastAPI + Uvicorn
- **Infra:** Docker, docker-compose

## Project structure

```
EnterpriseRAG/
├── app/
│   ├── main.py              # FastAPI entrypoint
│   ├── services/
│   │   ├── ingestion.py     # IngestionService — parses & chunks documents
│   │   ├── retrieval.py     # RetrievalService — semantic search
│   │   └── rag_service.py   # RAGService — end-to-end RAG query pipeline
│   └── database/
│       └── qdrant.py        # VectorStore — Qdrant collection management
├── chroma_db/                # local Chroma persistence
├── data/                      # uploaded source documents
├── tests/
├── test_ingestion.py          # sample: ingest a PDF
├── test_retrieval.py          # sample: run a retrieval query
├── test_rag.py                 # sample: run a full RAG query
├── test_qdrant.py              # sample: create a Qdrant collection
├── Dockerfile
├── docker-compose.yml          # spins up the Qdrant container
└── requirements.txt
```

## Getting started

### 1. Clone and install

```bash
git clone https://github.com/Akshita1906/EnterpriseRAG.git
cd EnterpriseRAG
pip install -r requirements.txt
```

### 2. Set environment variables

Create a `.env` file with your API keys:

```
GOOGLE_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

### 3. (Optional) Start Qdrant

If using the Qdrant backend instead of local Chroma:

```bash
docker-compose up -d
```

### 4. Ingest a document

```bash
python test_ingestion.py
```

### 5. Ask a question

```bash
python test_rag.py
```

### Or run as an API

```bash
docker build -t enterprise-rag .
docker run -p 8000:8000 enterprise-rag
```

## Why I built this

This mirrors the retrieval-augmented and agentic AI systems I work on professionally (LLM-powered chatbots and multi-agent banking assistants), built independently end-to-end — from document ingestion through vector retrieval to grounded LLM responses — with a swappable vector store backend to explore the trade-offs between a local, file-based store (Chroma) and a containerized, production-style one (Qdrant).

## Roadmap

- [ ] Expose ingestion/retrieval/RAG as REST endpoints in `app/main.py`
- [ ] Add a minimal front-end or Streamlit UI for interactive querying
- [ ] Add automated tests (pytest) beyond the manual test scripts
- [ ] Deploy a live demo
