from fastapi import APIRouter, File, UploadFile
import shutil
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse

router = APIRouter()

@router.get("/status")
async def status_check():
    return {"status" : "ok"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with open(f"uploads/{file.filename}", "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {"filename": file.filename}