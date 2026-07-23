# pyrefly: ignore [missing-import]
from fastapi import FastAPI, Request
# pyrefly: ignore [missing-import]
from fastapi.responses import JSONResponse

from app.core.logger import logger
from app.core.exceptions.custom_exceptions import (
    DocumentRetrievalError,
    LLMGenerationError,
    DocumentIngestionError
)

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(DocumentRetrievalError)
    async def document_retrieval_exception_handler(
        request: Request, 
        exc: DocumentRetrievalError):
        logger.exception(exc)
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)}
        )

    @app.exception_handler(LLMGenerationError)
    async def llm_generation_exception_handler(
        request: Request, 
        exc: LLMGenerationError
        ):
        logger.exception(exc)
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)}
        )

    @app.exception_handler(DocumentIngestionError)
    async def document_ingestion_exception_handler(
        request: Request, 
        exc: DocumentIngestionError
        ):
        logger.exception(exc)
        return JSONResponse(
            status_code=500,
            content={"error": str(exc)}
        )

    @app.exception_handler(Exception)
    async def generic_exception_handler(
        request: Request, 
        exc: Exception
        ):
        logger.exception(exc)
        return JSONResponse(
            status_code=500,
            content={"error": "An unexpected error occurred. Please try again later."}
        )