<img width="1216" height="596" alt="image" src="https://github.com/user-attachments/assets/405b0151-0a6e-4330-a350-b8dc44ba761c" />📌 프로젝트 개요

이 프로젝트는 BACnet/Modbus 장치 데이터를 시뮬레이션하고, SQLite DB에 저장하며, REST API와 WebSocket을 통해 데이터를 실시간으로 제공하는 백엔드 시스템입니다.
포트폴리오용으로 설계되었으며, 실제 AI DCIM/Smart BEMS 시스템에서 수행했던 데이터 수집, 실시간 모니터링, CRUD 작업, WebSocket 실시간 전송을 시뮬레이션합니다.
1. REST API
실행: 
uvicorn backend.api.rest:app --reload
모든 장치 데이터 확인:
http://127.0.0.1:8000/devices
<img width="2101" height="1453" alt="image" src="https://github.com/user-attachments/assets/9e1aed73-4a1b-4e7c-a43a-db0cd8ad0231" />

2. WEBSOCKET
<br># Terminal 1: DB initialization (once)
python -m backend.db.init_db
<img width="978" height="410" alt="image" src="https://github.com/user-attachments/assets/d71b6bd9-5db7-4569-b589-be5bc6660a26" />

<br># Terminal 2: Start cron job simulator
python -m backend.cron_jobs.fetch_device_data

<br># Terminal 3: Start WebSocket server
uvicorn backend.api.websocket:app --reload --port 8001

<br># Terminal 4: Serve frontend
python -m http.server 5500
<img width="1216" height="596" alt="image" src="https://github.com/user-attachments/assets/247c660f-fb9c-4d58-bcf4-06fb7dd1dc51" />

🏗️ 아키텍처 개요
[Simulated Devices] <br>
↓ <br>
[Cron Job / Device Simulator] <br>
↓ <br>
[SQLite DB] <br>
↓ <br>
[Backend (Python + FastAPI)] <br> - 1) REST API (/devices) <br> - 2) WebSocket (/ws/devices) <br>
↓ <br>
[WebSocket Test HTML Dashboard]<br>
(실시간 데이터 확인 및 시각화)

장치 데이터 시뮬레이션: BACnet/Modbus 장치를 모방하여 임의 데이터 생성

DB 저장: SQLite에 CRUD 저장, Cron Job으로 주기적 삽입

REST API: 데이터 조회를 위한 엔드포인트 제공

WebSocket: 실시간 데이터 푸시를 통해 클라이언트에서 즉시 확인 가능

프론트엔드: 단순 HTML/JS로 실시간 데이터를 표 형식으로 확인 가능

🛠️ 설치 및 실행 가이드
1️⃣ 장치 데이터 시뮬레이션
1-1. 데이터베이스 테이블 생성
python -m backend.db.init_db<br>

1-2. 장치 데이터 시뮬레이션 실행
python -m backend.devices.simulator <br>

1-3. Cron Job으로 주기적 데이터 삽입
python -m backend.cron_jobs.fetch_device_data
<br>

프로젝트 루트에서 실행하며, SQLite DB에 장치 데이터가 5초마다 삽입됩니다.

2️⃣ REST API 데이터 조회
uvicorn backend.api.rest:app --reload

모든 장치 데이터 확인:
http://127.0.0.1:8000/devices

3️⃣ WebSocket 실시간 데이터
3-1. WebSocket 서버 실행
uvicorn backend.api.websocket:app --reload --port 8001
<br>

3-2. 프론트엔드 테스트 서버 실행
python -m http.server 5500 <br>

3-3. WebSocket 클라이언트 접속

브라우저에서 다음 주소 열기:
http://127.0.0.1:5500/websocket.html <br>

WebSocket 서버에서 실시간으로 전송되는 장치 데이터를 HTML 페이지에서 확인할 수 있습니다.

4️⃣ 프로젝트 구조
SmartBEMS/ <br>
│ <br>
├─ backend/ <br>
│ ├─ devices/ <br>
│ │ └─ simulator.py # BACnet/Modbus 장치 데이터 시뮬레이터 <br>
│ │ <br>
│ ├─ db/ <br>
│ │ ├─ models.py # DB 모델 정의 (SQLAlchemy) <br>
│ │ └─ init_db.py # DB 초기화<br>
│ │ <br>
│ ├─ cron_jobs/ <br>
│ │ └─ fetch_device_data.py # 주기적 데이터 삽입 <br>
│ │ <br>
│ └─ api/ <br>
│ ├─ rest.py # REST API <br>
│ └─ websocket.py # WebSocket 서버 <br>
│ <br>
├─ frontend_test.html # 실시간 데이터 확인용 프론트엔드<br>
├─ requirements.txt<br>
└─ README.md<br>
<br>
5️⃣ 주요 특징

SQLite DB 기반 실시간 장치 데이터 시뮬레이션

REST API와 WebSocket으로 데이터 조회 및 실시간 푸시

간단한 HTML 프론트엔드로 실시간 데이터 시각화 가능

Cron Job으로 장치 데이터를 주기적으로 삽입, 실제 배치 환경 시뮬레이션

포트폴리오용으로 백엔드 전문성을 강조 가능
