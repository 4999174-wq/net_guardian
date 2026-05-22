# src/guide.py


def analyze_cause(features):

    # timeout 상태
    if features["success"] == 0:

        return "timeout"

    # 심각한 delay
    elif features["response_time_ms"] >= 500:

        return "critical_delay"

    # 일반 delay
    elif features["response_time_ms"] >= 150:

        return "delay"

    # 정상 상태
    else:

        return "normal"


GUIDE_DB = {

    "normal": {

        "cause": "정상 통신 상태",

        "action": "추가 조치 불필요"
    },

    "delay": {

        "cause": "네트워크 지연 발생",

        "action": "네트워크 부하 및 RTT 상태 점검"
    },

    "critical_delay": {

        "cause": "심각한 네트워크 지연 발생",

        "action": "스위치 및 시스템 상태 확인"
    },

    "timeout": {

        "cause": "패킷 손실 또는 timeout 발생",

        "action": "포트 상태 및 케이블 연결 점검"
    }
}
