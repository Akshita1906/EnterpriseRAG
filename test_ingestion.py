from app.services.ingestion import IngestionService

service = IngestionService()
service.ingest("data/uploads/linalg.pdf")