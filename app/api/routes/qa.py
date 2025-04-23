from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.api.deps.auth import verify_api_key
from app.services.qa_service import get_answer
from utils.logger import logger

router = APIRouter()


class AnswerRequest(BaseModel):
    provider: str
    model: str
    question: str


class AnswerResponse(BaseModel):
    answer: str


@router.post("/llm/get_answer", tags=["LLM"], response_model=AnswerResponse,
             dependencies=[Depends(verify_api_key)])
async def get_answer_from_llm(request: AnswerRequest):
    logger.info("LLM answer request received | Provider: %s | Model: %s | Question: %s",
                request.provider, request.model, request.question)

    try:
        answer = get_answer(request.provider, request.model, request.question)
        logger.info("LLM answer generated successfully.")
        return answer
    except Exception as e:
        logger.exception("Error while getting answer from LLM.")
        raise
