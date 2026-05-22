Ubuntu Linux 기반 Modbus/TCP 산업 네트워크 환경에서  
네트워크 지연(delay), packet loss, timeout 상태를  
Threshold 기반으로 탐지하는 시스템

---

# 프로젝트 개요

본 프로젝트는 산업 네트워크 환경에서 발생할 수 있는  
통신 지연 및 패킷 손실 상황을 실시간으로 탐지하기 위해 구현하였다.

실시간 Modbus/TCP 로그 데이터를 수집하고  
RTT(Response Time) 및 통신 성공 여부(success)를 분석하여  
현재 네트워크 상태를 판단한다.

또한 Streamlit 기반 대시보드를 통해  
실시간 모니터링이 가능하도록 구성하였다.

---

# 주요 기능

- Modbus/TCP 통신 로그 수집
- Threshold 기반 네트워크 상태 분석
- Delay 및 Packet Loss 탐지
- Rule 기반 원인 분석
- 대응 가이드 제공
- Streamlit 실시간 시각화

---

# 프로젝트 구조

```text
industrial-network-anomaly/
│
├── logs/
│   ├── normal.csv
│   └── realtime.csv
│
├── src/
│   ├── features.py
│   ├── train_model.py
│   ├── detector.py
│   ├── modbus_client.py
│   ├── streamlit_app.py
│   └── guide.py
│
├── analysis_result.csv
│
├── requirements.txt
├── README.md
└── run.sh