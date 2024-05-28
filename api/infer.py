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
    result = {"key1" : "value1" ,
              "key2" : "value1" ,
              "key3" : "value1" ,
              "key4" : {"subkey1" : "subval1",
                        "subkey2" : "subval2"} ,
              "key5" : "value5" ,
              }
    return result