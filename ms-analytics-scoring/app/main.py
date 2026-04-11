from fastapi import FastAPI
from routers.analytics_router import router as analytics_router

app = FastAPI(title="MS Analytics Scoring", version="1.0.0")

app.include_router(analytics_router, prefix="/analytics", tags=["analytics"])

@app.get("/")
async def root():
    return {"message": "MS Analytics Scoring is running"}