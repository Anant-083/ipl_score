import asyncio
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from manager import manager
from engine import get_live_scores, get_points_table
 
# Modern lifespan approach (replaces deprecated @app.on_event)
@asynccontextmanager
async def lifespan(app: FastAPI):
    task = asyncio.create_task(fetch_score_ticker())
    yield
    task.cancel()
 
app = FastAPI(lifespan=lifespan)
 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
# Serve frontend files (index.html, style.css, app.js) from /frontend folder
app.mount("/static", StaticFiles(directory="frontend"), name="static")
 
async def fetch_score_ticker():
    """
    Fetches scores every 5 minutes.
    Free RapidAPI tier: ~100-500 calls/month.
    5 min interval = ~8,640 calls/month — safe.
    """
    while True:
        try:
            print("Fetching fresh scores from Cricbuzz API...")
            scores, table = await asyncio.gather(get_live_scores(), get_points_table())
            payload = {**scores, "pointsTable": table}
            await manager.broadcast(payload)
            print(f"Broadcasted to {len(manager.active_connections)} connected client(s).")
        except Exception as e:
            print(f"Ticker Error: {e}")
        await asyncio.sleep(300)  # 5 minutes
 
@app.websocket("/ws/live")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        # Send immediately — don't make user wait 5 minutes
        scores, table = await asyncio.gather(get_live_scores(), get_points_table())
        payload = {**scores, "pointsTable": table}
        await websocket.send_json(payload)
 
        while True:
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)
 
@app.get("/")
async def root():
    return {"message": "IPL Live API is running. Connect via WebSocket at /ws/live"}
 