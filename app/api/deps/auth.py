from fastapi import Header, HTTPException
from utils.config import env_config
from utils.logger import logger

async def verify_api_key(api_key: str = Header(...)):
    if api_key != env_config.APP_API_KEY:
        logger.warning("Unauthorized access attempt with API key: %s", api_key)
        raise HTTPException(status_code=401, detail="Invalid API Key")
    logger.info("API key verification successful.")
