from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.data_router import router as data_router

app = FastAPI(title="BFF Gateway", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify allowed origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(data_router, prefix="", tags=["data"])

@app.get("/")
async def root():
    return {"message": "BFF Gateway is running"}