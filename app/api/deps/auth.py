import os
from fastapi import Header, HTTPException, Depends
from app.config import env_config

async def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != env_config.APP_API_KEY:
        raise HTTPException(status_code=401, detail="Invalid API Key")
