from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")


router = APIRouter()

@router.get("/status", response_class=HTMLResponse)
async def status_check():
    return "<p>OK</p>"

@router.get("/", response_class=RedirectResponse)
async def home():
    return RedirectResponse("/upload")

@router.get("/upload", response_class=HTMLResponse)
async def upload(request: Request):
    return templates.TemplateResponse(
        request=request, name="upload.html", context={"infer_upload": "/infer/upload"}
    )