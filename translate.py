import os

# 지정된 디렉토리 경로
directory = "./train"

# 디렉토리 내의 모든 폴더 목록을 가져옵니다.
folders = os.listdir(directory)

# 폴더 이름을 수동으로 입력하여 영어로 변경합니다.
translations = {
    "가구수정": "furniture_correction",
    "걸레받이수정": "mop_correction",
    "곰팡이": "mold",
    "꼬임": "twist",
    "녹오염": "corrosion",
    "들뜸": "swell",
    "면불량": "fabric_defect",
    "몰딩수정": "molding_correction",
    "반점": "stain",
    "석고수정": "plaster_correction",
    "오염": "contamination",
    "오타공": "typo_correction",
    "울음": "weep",
    "이음부불량": "seam_defect",
    "창틀,문틈수정": "window_frame_gap_correction",
    "터짐": "burst",
    "틈새과다": "excessive_gap",
    "피스": "piece",
    "훼손": "damage"
}

# 폴더 이름을 변경합니다.
for folder_name in folders:
    # 영어로 번역된 폴더 이름을 가져옵니다.
    translated_name = translations.get(folder_name)

    # 영어로 번역된 폴더 이름이 없는 경우, 원래 폴더 이름을 사용합니다.
    if translated_name is None:
        print(f"폴더 이름 '{folder_name}'의 번역이 없습니다. 원래 이름을 유지합니다.")
        translated_name = folder_name

    # 폴더의 현재 경로와 새로운 경로를 생성합니다.
    old_path = os.path.join(directory, folder_name)
    new_path = os.path.join(directory, translated_name)

    # 폴더 이름을 변경합니다.
    os.rename(old_path, new_path)