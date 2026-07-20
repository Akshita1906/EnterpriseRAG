# pyrefly: ignore [missing-import]
from langchain_huggingface import HuggingFaceEmbeddings

class EmbeddingModel:
    def __init__(self):
        self.embedding_model= HuggingFaceEmbeddings(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def get_model(self):
        return self.embedding_model