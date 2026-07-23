# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    APP_NAME: str = "Enterprise RAG Platform"
    APP_VERSION: str = "1.0.0"
    DEBUG: bool = True
    
    GOOGLE_API_KEY: str = ""

    # Vector Store Config
    QDRANT_URL: str = "http://localhost:6333"
    QDRANT_API_KEY: Optional[str] = None
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()