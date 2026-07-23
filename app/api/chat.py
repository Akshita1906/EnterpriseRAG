# pyrefly: ignore [missing-import]
from fastapi import APIRouter
# pyrefly: ignore [missing-import]
from app.schema.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter()
rag = RAGService()

@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    result = rag.ask(request.question)

    return ChatResponse(
        answer=result["answer"],
        citations=result["citations"]
    )