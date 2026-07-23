# pyrefly: ignore [missing-import]
from google import genai
from app.core.config import settings
from app.core.exceptions.custom_exceptions import LLMGenerationError
from app.core.logger import logger

class GeminiService:
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.client = genai.Client(api_key=settings.GOOGLE_API_KEY)
        self.model_name = model_name

    def generate(self, prompt: str) -> str:
        try:
            response = self.client.models.generate_content(
                model=self.model_name,
                contents=prompt,
            )
            return response.text

        except Exception as e:
            logger.exception(e)
            raise LLMGenerationError(str(e))
