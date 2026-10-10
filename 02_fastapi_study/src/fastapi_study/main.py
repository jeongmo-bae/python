from fastapi import FastAPI
from fastapi_study.routers.items import router as items_router

app = FastAPI()
app.include_router(items_router)

@app.get("/")
def read_root():
    return {"message": "안녕, FastAPI!"}
