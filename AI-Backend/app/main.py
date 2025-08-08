from fastapi import FastAPI
from .utils.db import connect_to_mongo, close_mongo_connection
from .api.lectures import router as lectures_router
from .api.process import router as process_router

app = FastAPI(title = "Lecture Summarizer API")

@app.on_event("startup")
async def startup_event():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown_event():
    await close_mongo_connection()

app.include_router(lectures_router, prefix = "/lectures", tags = ["lectures"])
app.include_router(process_router, prefix = "/lectures",tags["process"])


@app.get("/")
async def read_root():
    return {"status": "ok"}