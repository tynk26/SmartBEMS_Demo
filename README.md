1. Simulate BACnet Device Data
   1-1. Create Database Tables Using SQLite
   python -m backend.db.init_db

1-2. Simulate Device Data
python backend/devices/simulator.py

1-3. Run CRON Job For CRUD (as a module from project root)
python -m backend.cron_jobs.fetch_device_data

<img width="962" height="369" alt="image" src="https://github.com/user-attachments/assets/fbbc5955-66f3-442f-b59a-ae57e7d9ecc2" />
<img width="1051" height="727" alt="image" src="https://github.com/user-attachments/assets/82649937-868c-4cf0-a5c2-fcd1e7b9eeeb" />


<img width="1050" height="732" alt="image" src="https://github.com/user-attachments/assets/90c2232e-d20a-4819-9d7e-9bfab91bb6f5" />

2. REST API for Data Polling
   uvicorn backend.api.rest:app --reload
   http://127.0.0.1:8000/devices
   <img width="1022" height="309" alt="image" src="https://github.com/user-attachments/assets/014d2305-b7f2-406b-b9ec-57a8bd4fa7ab" />

3. WebSocket for Continuous Server Pushing to Client (websocket.html)
   3-1. RUN Websocket Server
   uvicorn backend.api.websocket:app --reload --port 8001
   3-2. RUN CRON job
   python -m http.server 5500
   3.3. Check Websocket Client
   http://127.0.0.1:5500/frontend_test.html

<img width="1121" height="717" alt="image" src="https://github.com/user-attachments/assets/43f8d93a-1760-4ed6-bfbc-193d0d7cbb5a" />

