from fastapi import FastAPI
from .routers.ml_router import router as ml_router

app = FastAPI(title="MS ML", version="1.0.0")

app.include_router(ml_router, prefix="/ml", tags=["ml"])

@app.get("/")
async def root():
    return {"message": "MS ML is running"}