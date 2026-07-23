# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, field_validator


class Citation(BaseModel):
    source: str
    page: int


class ChatRequest(BaseModel):
    question: str = Field(
        ...,
        min_length=3,
        max_length=1000
    )

    @field_validator("question")
    @classmethod
    def validate_question(cls, value: str):
        if not value.strip():
            raise ValueError("Question cannot be empty.")
        return value.strip()


class ChatResponse(BaseModel):
    answer: str
    citations: list[Citation]