# pyrefly: ignore [missing-import]
from langchain_chroma import Chroma 
from app.embeddings.embedding_model import EmbeddingModel

class ChromaStore:
    def __init__(self):
        self.embedding=EmbeddingModel().get_model()
        self.vector_store = Chroma(
            collection_name="enterprise_rag",
            embedding_function=self.embedding,
            persist_directory="./chroma_db"
        )

    def get_vector_store(self):
        return self.vector_store