from fastapi import FastAPI
from .routers.ingestion_router import router as ingestion_router

app = FastAPI(title="MS Ingestion", version="1.0.0")

app.include_router(ingestion_router, prefix="/ingestion", tags=["ingestion"])

@app.get("/")
async def root():
    return {"message": "MS Ingestion is running"}