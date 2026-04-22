import asyncio
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from engine import get_live_scores, get_points_table

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="frontend"), name="static")

@app.get("/api/live")
async def live_data():
    scores, table = await asyncio.gather(get_live_scores(), get_points_table())
    return {**scores, "pointsTable": table}

@app.get("/")
async def root():
    return {"message": "IPL Live API is running."}