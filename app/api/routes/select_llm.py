from fastapi import APIRouter, Depends
from pydantic import BaseModel
from typing import Dict, List
from app.api.deps.auth import verify_api_key
from app.services.llm_options import fetch_llm_options
from app.logger import logger

router = APIRouter()


class LLMOptionsResponse(BaseModel):
    Groq: List[str]
    Ollama: List[str]
    Openai: List[str]


@router.get("/llm/llm_options",
            tags=["LLM"],
            response_model=LLMOptionsResponse,
            dependencies=[Depends(verify_api_key)])
async def provide_llm_options():
    logger.info("Fetching available LLM options.")

    try:
        llm_details = fetch_llm_options()
        logger.info("LLM options fetched successfully.")
        return llm_details
    except Exception as e:
        logger.exception("Failed to fetch LLM options.")
        raise
