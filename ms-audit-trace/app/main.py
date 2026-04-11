from fastapi import FastAPI
from .routers.audit_router import router as audit_router

app = FastAPI(title="MS Audit Trace", version="1.0.0")

app.include_router(audit_router, prefix="/audit", tags=["audit"])

@app.get("/")
async def root():
    return {"message": "MS Audit Trace is running"}