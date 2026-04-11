from fastapi import FastAPI
from routers.transformation_router import router as transformation_router

app = FastAPI(title="MS Transformation", version="1.0.0")

app.include_router(transformation_router, prefix="/transformation", tags=["transformation"])

@app.get("/")
async def root():
    return {"message": "MS Transformation is running"}