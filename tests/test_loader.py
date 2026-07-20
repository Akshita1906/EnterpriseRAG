from app.loaders.pdf_loader import PDFLoader
from app.services.text_splitter import DocumentSplitter

loader=PDFLoader("data/uploads/linalg.pdf")

documents=loader.load()

splitter = DocumentSplitter()

chunks=splitter.split(documents)

print(f"Pages: {len(documents)}")
print(f"Chunks: {len(chunks)}")
print("\nFirst Chunk:\n")
print(chunks[0].page_content)
