class DocumentRetrievalError(Exception):
    """Raised when document retrieval fails"""
    pass
    
class LLMGenerationError(Exception):
    """Raised when LLM generation fails"""
    pass


class DocumentIngestionError(Exception):
    """Raised when document ingestion fails"""
    pass