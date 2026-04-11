from fastapi import FastAPI
from .routers.recommendations_router import router as recommendations_router

app = FastAPI(title="MS Recommendations", version="1.0.0")

app.include_router(recommendations_router, prefix="/recommendations", tags=["recommendations"])

@app.get("/")
async def root():
    return {"message": "MS Recommendations is running"}