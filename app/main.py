# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from app.api.chat import router as chat_router
from app.api.health import router as health_router

# pyrefly: ignore [missing-import]
from app.core.exceptions.handlers import register_exception_handlers

app = FastAPI(title="Enterprise RAG")

#register exception handlers
register_exception_handlers(app)

app.include_router(chat_router)
app.include_router(health_router)

