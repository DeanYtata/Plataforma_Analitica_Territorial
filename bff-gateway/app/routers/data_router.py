from fastapi import APIRouter, HTTPException
import httpx

router = APIRouter()

@router.get("/data")
async def get_data():
    # Example: Aggregate data from ms-ingestion and ms-analytics
    async with httpx.AsyncClient() as client:
        try:
            ingestion_response = await client.get("http://ms-ingestion:8000/ingestion/")
            analytics_response = await client.get("http://ms-analytics-scoring:8000/analytics/score")
            return {
                "ingestion": ingestion_response.json(),
                "analytics": analytics_response.json()
            }
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))