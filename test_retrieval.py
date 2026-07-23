from app.services.retrieval import RetrievalService

retriever = RetrievalService()

query = input("Ask a question: ")

results = retriever.retrieve(query)

for i, doc in enumerate(results,start=1):
    print(f"---Result {i}----")
    print("-"*80)

    print(doc.page_content)
    print("\Metadata:")
    print(doc.metadata)
    print("="*80)

