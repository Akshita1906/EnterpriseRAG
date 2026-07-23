# pyrefly: ignore [missing-import]
from langchain_qdrant import QdrantVectorStore
# pyrefly: ignore [missing-import]
from qdrant_client import QdrantClient
# pyrefly: ignore [missing-import]
from qdrant_client.models import VectorParams, Distance

from app.core.config import settings
from app.embeddings.embedding_model import EmbeddingModel


class VectorStore:
    def __init__(self):
        self.client = QdrantClient(
            url=settings.QDRANT_URL
        )
        self.embedding = EmbeddingModel().get_model()

    def create_collection(self):
        if not self.client.collection_exists("enterprise_rag"):
            self.client.create_collection(
                collection_name="enterprise_rag",
                vectors_config=VectorParams(size=384, distance=Distance.COSINE)
            )

    def get_vector_store(self):
        return QdrantVectorStore.from_existing_collection(
            client=self.client,
            collection_name="enterprise_rag",
            embedding=self.embedding
        )