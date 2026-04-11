from fastapi import APIRouter

router = APIRouter()

@router.get("/score")
async def get_score():
    # Placeholder for scoring logic
    return {"score": 85, "status": "success"}