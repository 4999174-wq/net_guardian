# Threshold 기반 산업 네트워크 장애 탐지

import pandas as pd

from features import extract_features

from guide import analyze_cause


# -----------------------------
# Threshold 설정
# -----------------------------

DELAY_THRESHOLD = 150

CRITICAL_DELAY = 500


# -----------------------------
# 상태 판단 함수
# -----------------------------
def analyze_network(response_time_ms, success):

    # timeout 상태
    if success == 0:

        return "timeout"

    # 심각한 지연
    elif response_time_ms >= CRITICAL_DELAY:

        return "critical_delay"

    # 일반 지연
    elif response_time_ms >= DELAY_THRESHOLD:

        return "delay"

    # 정상 상태
    else:

        return "normal"


# -----------------------------
# 전체 로그 분석 함수
# -----------------------------
def detect_anomaly(df):

    results = []

    for _, row in df.iterrows():

        # feature 추출
        features = extract_features(row)

        # 상태 탐지
        status = analyze_network(

            features["response_time_ms"],

            features["success"]
        )

        # 원인 분석
        guide = analyze_cause(status)

        # 결과 저장
        results.append({

            "timestamp":
            row["timestamp"],

            "response_time_ms":
            features["response_time_ms"],

            "success":
            features["success"],

            "real_scenario":
            row["scenario"],

            "predicted_status":
            status,

            "cause":
            guide["cause"],

            "action":
            guide["action"]
        })

    return pd.DataFrame(results)


# -----------------------------
# 단독 실행 테스트
# -----------------------------
if __name__ == "__main__":

    columns = [

        "timestamp",

        "response_time_ms",

        "success",

        "scenario"
    ]

    df = pd.read_csv(

        "logs/normal.csv",

        names=columns,

        skiprows=1
    )

    result_df = detect_anomaly(df)

    print("\n========== Analysis Result ==========\n")

    print(result_df.head(50))

    print("\n=====================================\n")

    # 결과 저장
    result_df.to_csv(

        "analysis_result.csv",

        index=False
    )

    print("analysis_result.csv saved")
