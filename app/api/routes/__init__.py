from fastapi import APIRouter
from app.api.routes.health import router as health_router
from app.api.routes.select_llm import router as llm_selection_router
from app.api.routes.qa import router as get_answer_router

router = APIRouter()
router.include_router(health_router)
router.include_router(llm_selection_router)
router.include_router(get_answer_router)
