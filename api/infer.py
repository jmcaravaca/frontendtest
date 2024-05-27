from fastapi import APIRouter
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse

router = APIRouter()

@router.get("/status")
async def status_check():
    return {"status" : "ok"}