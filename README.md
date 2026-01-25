1. Simulate BACnet Device Data
   1-1. Create Database Tables Using SQLite
   python -m backend.db.init_db

1-2. Simulate Device Data
python backend/devices/simulator.py

1-3. Run CRON Job For CRUD (as a module from project root)
python -m backend.cron_jobs.fetch_device_data


2. REST API for Data Polling
   uvicorn backend.api.rest:app --reload
   http://127.0.0.1:8000/devices

3. WebSocket for Continuous Server Pushing to Client (websocket.html)
   3-1. RUN Websocket Server
   uvicorn backend.api.websocket:app --reload --port 8001
   3-2. RUN CRON job
   python -m http.server 5500
   3.3. Check Websocket Client
   http://127.0.0.1:5500/frontend_test.html


