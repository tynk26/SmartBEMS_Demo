from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class DeviceData(Base):
    __tablename__ = "device_data"

    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(String, index=True)
    device_type = Column(String)
    temperature = Column(Float)
    humidity = Column(Float)
    energy = Column(Float)
    status = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)
