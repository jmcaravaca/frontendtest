from fastapi import APIRouter

from .frontend import router as frontendrouter
from .infer import router as inferrouter

router = APIRouter()

router.include_router(frontendrouter, prefix="", tags=["front"])
router.include_router(inferrouter, prefix="/infer", tags=["api"])
