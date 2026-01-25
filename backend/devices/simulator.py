import random
from datetime import datetime

DEVICE_TYPES = ["HVAC", "Chiller", "Lighting", "Sensor"]

def generate_device_data(device_id: str):
    return {
        "device_id": device_id,
        "device_type": random.choice(DEVICE_TYPES),
        "temperature": round(random.uniform(18, 30), 2),
        "humidity": round(random.uniform(30, 70), 2),
        "energy": round(random.uniform(0, 5), 2),
        "status": random.choice(["ON", "OFF", "MAINTENANCE"]),
        "timestamp": datetime.utcnow()
    }

# Quick test
if __name__ == "__main__":
    for i in range(3):
        print(generate_device_data(f"device_{i+1}"))
