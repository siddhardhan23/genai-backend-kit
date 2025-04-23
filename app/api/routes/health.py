from fastapi import APIRouter
from utils.logger import logger

router = APIRouter()

@router.get("/health", tags=["Health"])
async def health_check():
    logger.info("Health check endpoint called.")
    return {"status": "ok"}
