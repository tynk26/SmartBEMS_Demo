from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from backend.db.init_db import SessionLocal
from backend.db.models import DeviceData
from fastapi.middleware.cors import CORSMiddleware
from typing import List

app = FastAPI(title="SmartBEMS API")

# Allow all origins for testing
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# DB session dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint: return all device data
@app.get("/devices", response_model=List[dict])
def get_all_devices(db: Session = Depends(get_db)):
    devices = db.query(DeviceData).order_by(DeviceData.timestamp.desc()).all()
    return [vars(d) for d in devices]

# Endpoint: return latest reading per device
@app.get("/devices/latest", response_model=List[dict])
def get_latest_devices(db: Session = Depends(get_db)):
    devices = db.query(DeviceData.device_id).distinct().all()
    result = []
    for device_id_tuple in devices:
        device_id = device_id_tuple[0]
        latest = (
            db.query(DeviceData)
            .filter(DeviceData.device_id == device_id)
            .order_by(DeviceData.timestamp.desc())
            .first()
        )
        if latest:
            result.append(vars(latest))
    return result

