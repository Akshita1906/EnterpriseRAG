from app.loaders.pdf_loader import PDFLoader

loader=PDFLoader("data/uploads/linalg.pdf")

documents=loader.load()

print(documents[0])
