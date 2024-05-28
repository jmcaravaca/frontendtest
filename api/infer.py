from fastapi import APIRouter, File, UploadFile
import shutil, os
from fastapi.responses import JSONResponse, RedirectResponse, HTMLResponse

router = APIRouter()

@router.get("/status")
async def status_check():
    return {"status" : "ok"}

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    os.makedirs("uploads" , exist_ok=True)
    local_filepath = f"uploads/{file.filename}"
    with open(local_filepath, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    results = inference_test(local_filepath)
    return results

def inference_test(filepath: str):
    print(f"Fake inference for: {filepath}")
    lorem = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum."
    result = {"key1" : lorem ,
              "key2" : lorem ,
              "key3" : lorem ,
              "key4" : {"subkey1" : lorem,
                        "subkey2" : lorem} ,
              "key5" : lorem ,
              }
    return result