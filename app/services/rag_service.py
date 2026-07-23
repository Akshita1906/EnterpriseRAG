from app.services.retrieval import RetrievalService
from app.llm.gemini import GeminiService


class RAGService:
    def __init__(self):
        self.retriever=RetrievalService()
        self.llm=GeminiService()

    
    def ask(self,question:str,k:int=4):
        #Retrieve context
        documents=self.retriever.retrieve(question,k)
        context = "\n\n".join(doc.page_content for doc in documents)

        prompt = f"""
        You are a helpful AI assistant. 
        Answer ONLY using the context below. 
        If the answer is not present in the context, 
        reply: 'I couldn't find that information in the provided documents.'
        
        Context: {context}
        
        Question: {question}
        
        Answer:
        """

        answer = self.llm.generate(prompt)

        # Extract citations
        seen = set()
        citations = []

        for doc in documents:
            key = (
                doc.metadata.get("source"),
                doc.metadata.get("page")
            )
            if key not in seen:
                seen.add(key)
                citations.append({
                    "source":key[0],
                    "page":key[1]
                })
        return {
            "answer": answer,
            "citations": citations
        }
