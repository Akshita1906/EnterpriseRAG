from app.database.qdrant import VectorStore

db = VectorStore()
db.create_collection()

print("collection created successfully")