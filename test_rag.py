from app.services.rag_service import RAGService

rag = RAGService()

while True:
    query = input("Ask a question (type 'quit' to exit): ")
    if query.lower() == "quit":
        break

    print(rag.ask(query))
    print("-"*80)