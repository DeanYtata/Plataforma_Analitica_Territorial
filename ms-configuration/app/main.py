from fastapi import FastAPI
from .routers.config_router import router as config_router

app = FastAPI(title="MS Configuration", version="1.0.0")

app.include_router(config_router, prefix="/config", tags=["config"])

@app.get("/")
async def root():
    return {"message": "MS Configuration is running"}