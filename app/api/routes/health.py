from fastapi import APIRouter, Depends
from app.api.deps.auth import verify_api_key

router = APIRouter()

@router.get("/health", tags=["Health"], dependencies=[Depends(verify_api_key)])
async def health_check():
    return {"status": "ok"}
