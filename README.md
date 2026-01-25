1. Simulate BACnet Device Data
   1-1. Create Database Tables Using SQLite
   python -m backend.db.init_db

1-2. Simulate Device Data
python backend/devices/simulator.py

1-3. Run CRON Job For CRUD (as a module from project root)
python -m backend.cron_jobs.fetch_device_data

<img width="962" height="369" alt="image" src="https://github.com/user-attachments/assets/fbbc5955-66f3-442f-b59a-ae57e7d9ecc2" />

2. REST API for Data Polling
   uvicorn backend.api.rest:app --reload
   http://127.0.0.1:8000/devices
   <img width="1022" height="309" alt="image" src="https://github.com/user-attachments/assets/014d2305-b7f2-406b-b9ec-57a8bd4fa7ab" />

3. WebSocket for Server Pushing
   uvicorn backend.api.websocket:app --reload --port 8001
   The websocket server runs at ws://127.0.0.1:8001/ws/devices
