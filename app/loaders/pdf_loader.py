# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import PyMuPDFLoader

class PDFLoader:
    def __init__(self, file_path:str):
        self.file_path = file_path

    def load(self):
        loader = PyMuPDFLoader(self.file_path)
        documents=loader.load()

        return documents
        
        