📌 프로젝트 개요

이 프로젝트는 BACnet/Modbus 장치 데이터를 시뮬레이션하고, SQLite DB에 저장하며, REST API와 WebSocket을 통해 데이터를 실시간으로 제공하는 백엔드 시스템입니다.
포트폴리오용으로 설계되었으며, 실제 AI DCIM/Smart BEMS 시스템에서 수행했던 데이터 수집, 실시간 모니터링, CRUD 작업, WebSocket 실시간 전송을 시뮬레이션합니다.

🏗️ 아키텍처 개요
🏗️ 아키텍처 개요
[Simulated Devices]
    ↓
[Cron Job / Device Simulator]
    ↓
[SQLite DB]
    ↓
[Backend (Python + FastAPI)]
    - 1) REST API (/devices)
    - 2) WebSocket (/ws/devices)
    ↓
[WebSocket Test HTML Dashboard]
    (실시간 데이터 확인 및 시각화)



장치 데이터 시뮬레이션: BACnet/Modbus 장치를 모방하여 임의 데이터 생성

DB 저장: SQLite에 CRUD 저장, Cron Job으로 주기적 삽입

REST API: 데이터 조회를 위한 엔드포인트 제공

WebSocket: 실시간 데이터 푸시를 통해 클라이언트에서 즉시 확인 가능

프론트엔드: 단순 HTML/JS로 실시간 데이터를 표 형식으로 확인 가능

🛠️ 설치 및 실행 가이드
1️⃣ 장치 데이터 시뮬레이션
1-1. 데이터베이스 테이블 생성
python -m backend.db.init_db

1-2. 장치 데이터 시뮬레이션 실행
python backend/devices/simulator.py

1-3. Cron Job으로 주기적 데이터 삽입
python -m backend.cron_jobs.fetch_device_data


프로젝트 루트에서 실행하며, SQLite DB에 장치 데이터가 5초마다 삽입됩니다.

2️⃣ REST API 데이터 조회
uvicorn backend.api.rest:app --reload


모든 장치 데이터 확인:
http://127.0.0.1:8000/devices

3️⃣ WebSocket 실시간 데이터
3-1. WebSocket 서버 실행
uvicorn backend.api.websocket:app --reload --port 8001

3-2. 프론트엔드 테스트 서버 실행
python -m http.server 5500

3-3. WebSocket 클라이언트 접속

브라우저에서 다음 주소 열기:
http://127.0.0.1:5500/websocket.html

WebSocket 서버에서 실시간으로 전송되는 장치 데이터를 HTML 페이지에서 확인할 수 있습니다.

4️⃣ 프로젝트 구조
SmartBEMS/
│
├─ backend/
│   ├─ devices/
│   │   └─ simulator.py          # BACnet/Modbus 장치 데이터 시뮬레이터
│   │
│   ├─ db/
│   │   ├─ models.py             # DB 모델 정의 (SQLAlchemy)
│   │   └─ init_db.py            # DB 초기화
│   │
│   ├─ cron_jobs/
│   │   └─ fetch_device_data.py  # 주기적 데이터 삽입
│   │
│   └─ api/
│       ├─ rest.py               # REST API
│       └─ websocket.py          # WebSocket 서버
│
├─ frontend_test.html            # 실시간 데이터 확인용 프론트엔드
├─ requirements.txt
└─ README.md

5️⃣ 주요 특징

SQLite DB 기반 실시간 장치 데이터 시뮬레이션

REST API와 WebSocket으로 데이터 조회 및 실시간 푸시

간단한 HTML 프론트엔드로 실시간 데이터 시각화 가능

Cron Job으로 장치 데이터를 주기적으로 삽입, 실제 배치 환경 시뮬레이션

포트폴리오용으로 백엔드 전문성을 강조 가능
