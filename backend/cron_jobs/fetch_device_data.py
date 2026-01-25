from backend.db.init_db import SessionLocal
from backend.db.models import DeviceData
from backend.devices.simulator import generate_device_data
import time

DEVICE_IDS = [f"device_{i}" for i in range(1, 4)]  # 3 devices for demo

def save_device_data():
    db = SessionLocal()
    try:
        for device_id in DEVICE_IDS:
            data = generate_device_data(device_id)
            db_entry = DeviceData(**data)
            db.add(db_entry)
        db.commit()
        print("Device data saved successfully.")
    except Exception as e:
        db.rollback()
        print("Error:", e)
    finally:
        db.close()

if __name__ == "__main__":
    # Run once every 5 seconds for testing
    while True:
        save_device_data()
        time.sleep(5)
