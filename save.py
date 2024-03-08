import pandas as pd
from test import predicted_classes

# 클래스 설명
descriptions = {
    "furniture_correction": "가구수정",
    "mop_correction": "걸레받이수정",
    "mold": "곰팡이",
    "twist": "꼬임",
    "corrosion": "녹오염",
    "swell": "들뜸",
    "fabric_defect": "면불량",
    "molding_correction": "몰딩수정",
    "stain": "반점",
    "plaster_correction": "석고수정",
    "contamination": "오염",
    "typo_correction": "오타공",
    "weep": "울음",
    "seam_defect": "이음부불량",
    "window_frame_gap_correction": "창틀,문틈수정",
    "burst": "터짐",
    "excessive_gap": "틈새과다",
    "piece": "피스",
    "damage": "훼손"
}

# 결과 데이터프레임 생성
df = pd.DataFrame({"id": [f"TEST_{i:03}" for i in range(len(predicted_classes))],
                   "label": predicted_classes})

# 클래스 이름을 설명으로 매핑
df['label'] = df['label'].map(descriptions)

# CSV 파일로 저장
df.to_csv("predictions_layer5.csv", index=False)
