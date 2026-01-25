from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware
from backend.db.init_db import SessionLocal
from backend.db.models import DeviceData
from datetime import datetime
import asyncio

app = FastAPI()

# Allow local frontend to connect
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can lock this to ["http://127.0.0.1:5500"] for security
    allow_methods=["*"],
    allow_headers=["*"],
)

# Connected WebSocket clients
clients = []

async def broadcast_data():
    """
    Fetch latest device data from DB every 60 seconds and push to all connected clients.
    """
    while True:
        db = SessionLocal()
        try:
            # Get the latest record for each device
            subquery = db.query(DeviceData.device_id, 
                                DeviceData.timestamp).distinct(DeviceData.device_id).subquery()
            latest_devices = (
                db.query(DeviceData)
                .join(subquery, (DeviceData.device_id == subquery.c.device_id) & (DeviceData.timestamp == subquery.c.timestamp))
                .all()
            )
            payload = [
                {
                    "device_id": d.device_id,
                    "device_type": d.device_type,
                    "temperature": d.temperature,
                    "humidity": d.humidity,
                    "energy": d.energy,
                    "status": d.status,
                    "timestamp": d.timestamp.isoformat()
                }
                for d in latest_devices
            ]
            for ws in clients:
                await ws.send_json(payload)
        finally:
            db.close()
        await asyncio.sleep(60)

@app.on_event("startup")
async def startup_event():
    # Start background broadcast task
    asyncio.create_task(broadcast_data())

@app.websocket("/ws/devices")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)
    print(f"Client connected: {len(clients)} clients total")
    try:
        while True:
            await websocket.receive_text()  # Keep connection alive; frontend may ping if needed
    except WebSocketDisconnect:
        clients.remove(websocket)
        print(f"Client disconnected: {len(clients)} clients total")


# clients = []
# @app.websocket("/ws/devices")
# async def websocket_endpoint(ws: WebSocket):
#     await ws.accept()  # accept client connection
#     clients.append(ws)
#     print("Client connected")
    
#     try:
#         while True:
#             # 1️⃣ Open a DB session
#             db = SessionLocal()

#             # 2️⃣ Get distinct device IDs
#             device_ids = db.query(DeviceData.device_id).distinct().all()

#             result = []
#             for device_id_tuple in device_ids:
#                 device_id = device_id_tuple[0]
#                 latest = (
#                     db.query(DeviceData)
#                     .filter(DeviceData.device_id == device_id)
#                     .order_by(DeviceData.timestamp.desc())
#                     .first()
#                 )
#                 if latest:
#                     result.append({
#                         "device_id": latest.device_id,
#                         "temperature": latest.temperature,
#                         "humidity": latest.humidity,
#                         "energy": latest.energy,
#                         "status": latest.status,
#                         "timestamp": str(latest.timestamp)
#                     })
#             db.close()

#             # 3️⃣ Send JSON data to this client
#             await ws.send_json(result)

#             # 4️⃣ Wait before next update
#             await asyncio.sleep(5)

#     except WebSocketDisconnect:
#         clients.remove(ws)
#         print("Client disconnected")
