from backend.devices.simulator import generate_device_data, DEVICES
from backend.db.init_db import SessionLocal
from backend.db.models import DeviceData
from datetime import datetime

def fetch_device_data():
    """
    Fetch simulated device data and insert into DB.
    Each device generates new values while keeping device_id and device_type fixed.
    """
    db = SessionLocal()
    try:
        for device in DEVICES:
            data = generate_device_data(device)
            # Insert as new row
            record = DeviceData(
                device_id=data["device_id"],
                device_type=data["device_type"],
                temperature=data["temperature"],
                humidity=data["humidity"],
                energy=data["energy"],
                status=data["status"],
                timestamp=data["timestamp"]
            )
            db.add(record)
        db.commit()
        print(f"[{datetime.utcnow()}] Inserted/Updated {len(DEVICES)} devices")
    finally:
        db.close()

if __name__ == "__main__":
    # Continuous simulation for testing
    import time
    while True:
        fetch_device_data()
        time.sleep(5)

# from backend.db.init_db import SessionLocal
# from backend.db.models import DeviceData
# from backend.devices.simulator import generate_device_data
# import time

# DEVICE_IDS = [f"device_{i}" for i in range(1, 20)]  # 20 devices for demo

# def save_device_data():
#     db = SessionLocal()
#     try:
#         for device_id in DEVICE_IDS:
#             data = generate_device_data(device_id)
#             db_entry = DeviceData(**data)
#             db.add(db_entry)
#         db.commit()
#         print("Device data saved successfully.")
#     except Exception as e:
#         db.rollback()
#         print("Error:", e)
#     finally:
#         db.close()

# if __name__ == "__main__":
#     # Run once every 5 seconds for testing
#     while True:
#         save_device_data()
#         time.sleep(5)
