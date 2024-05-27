from fastapi import FastAPI
from api import router
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.include_router(router)
app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5987)