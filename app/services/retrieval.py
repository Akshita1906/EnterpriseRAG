from app.vectorstore.chroma_store import ChromaStore
from app.core.logger import logger
from app.core.exceptions.custom_exceptions import DocumentRetrievalError


class RetrievalService:
    def __init__(self):
        self.vector_store = ChromaStore().get_vector_store()

    def retrieve(self,query: str,k:int=4):
        try:
            logger.info(f"Retrieving documents for query: {query}")
            documents=self.vector_store.similarity_search(query=query,k=k)
            logger.info(f"Retrieved {len(documents)} documents")
            logger.info(f"Returning retrieved documents")
            return documents
        except Exception as e:
            logger.exception(e)
            raise DocumentRetrievalError(str(e))

    