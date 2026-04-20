from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from typing import Dict, Any

from modules.core_ai import analyze_ticket_async, describe_surroundings_async
from modules.maps_logic import fetch_route_async
from modules.firebase_sync import QueueManager

app = FastAPI(title="VibeFlow AI Backend API")
queue_manager = QueueManager()

class RouteRequest(BaseModel):
    current_location: str
    destination: str

@app.post("/api/vision/analyze")
async def analyze_vision_input(file: UploadFile = File(...)) -> Dict[str, Any]:
    content = await file.read()
    return await analyze_ticket_async(content)

@app.post("/api/vision/describe")
async def describe_vision_input(file: UploadFile = File(...)) -> Dict[str, Any]:
    content = await file.read()
    return await describe_surroundings_async(content)

@app.post("/api/routing/optimal")
async def get_optimal_route(request: RouteRequest) -> Dict[str, Any]:
    return await fetch_route_async(request.current_location, request.destination)

@app.post("/api/queue/trigger")
async def trigger_queue(user_id: str, item_id: str) -> Dict[str, Any]:
    return await queue_manager.fresh_drop_alert_queue(user_id, item_id)

@app.get("/health")
def health_check():
    return {"status": "ok"}
