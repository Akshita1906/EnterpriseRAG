from app.loaders.pdf_loader import PDFLoader
from app.services.text_splitter import DocumentSplitter
from app.vectorstore.chroma_store import ChromaStore
from app.core.logger import logger

class IngestionService:
    def __init__(self):
        self.splitter = DocumentSplitter()
        self.vector_store = ChromaStore()

    def ingest(self, file_path: str):
        logger.info(f"Ingesting document: {file_path}")
        loader = PDFLoader(file_path)
        documents = loader.load()
        print(f"Loaded {len(documents)} pages")
        chunks = self.splitter.split(documents)
        logger.info(f"Split {len(chunks)} chunks")
        vector_store=self.vector_store.get_vector_store()
        vector_store.add_documents(chunks)
        logger.info("documents successfully stored in db")
        