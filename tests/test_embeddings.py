from app.embeddings.embedding_model import EmbeddingModel

embedding_model=EmbeddingModel().get_model()

text = "FastAPI is a python framework"
vector = embedding_model.embed_query(text)

print(len(vector))
print(vector[:10])