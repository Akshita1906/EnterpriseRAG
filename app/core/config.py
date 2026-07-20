# pyrefly: ignore [missing-import]
from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    APP_NAME:str
    APP_VERSION:str
    DEBUG:bool
    
    GOOGLE_API_KEY:str

    # Vector Store Config
    QDRANT_URL:str
    QDRANT_API_KEY:str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )

settings = Settings()