from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from backend.db.init_db import SessionLocal
from backend.db.models import DeviceData
import asyncio

app = FastAPI(title="SmartBEMS WebSocket")

clients = []
@app.websocket("/ws/devices")
async def websocket_endpoint(ws: WebSocket):
    await ws.accept()  # accept client connection
    clients.append(ws)
    print("Client connected")
    
    try:
        while True:
            # 1️⃣ Open a DB session
            db = SessionLocal()

            # 2️⃣ Get distinct device IDs
            device_ids = db.query(DeviceData.device_id).distinct().all()

            result = []
            for device_id_tuple in device_ids:
                device_id = device_id_tuple[0]
                latest = (
                    db.query(DeviceData)
                    .filter(DeviceData.device_id == device_id)
                    .order_by(DeviceData.timestamp.desc())
                    .first()
                )
                if latest:
                    result.append({
                        "device_id": latest.device_id,
                        "temperature": latest.temperature,
                        "humidity": latest.humidity,
                        "energy": latest.energy,
                        "status": latest.status,
                        "timestamp": str(latest.timestamp)
                    })
            db.close()

            # 3️⃣ Send JSON data to this client
            await ws.send_json(result)

            # 4️⃣ Wait before next update
            await asyncio.sleep(5)

    except WebSocketDisconnect:
        clients.remove(ws)
        print("Client disconnected")
