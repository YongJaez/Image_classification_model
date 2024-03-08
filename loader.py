
import os
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
import torchvision.transforms as transforms

class Data(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []

        # 클래스 이름을 저장할 리스트
        self.class_names = []
        # 클래스 이름과 해당 클래스에 대한 정수 레이블을 매핑하기 위한 딕셔너리
        self.class_label_map = {}
        label_index = 0

        # 디렉토리 내의 이미지 파일을 스캔하고 클래스 이름 추출
        for root, dirs, files in os.walk(root_dir):
            for filename in files:
                if filename.endswith(".png"):
                    filepath = os.path.join(root, filename)
                    class_name = os.path.basename(root)  # 이미지가 속한 폴더의 이름을 클래스 이름으로 사용

                    # 클래스 이름이 class_label_map에 없으면 새로운 정수 레이블 할당
                    if class_name not in self.class_label_map:
                        self.class_label_map[class_name] = label_index
                        self.class_names.append(class_name)
                        label_index += 1

                    image = Image.open(filepath).convert("RGB")
                    # 이미지 전처리
                    if self.transform:
                        image = self.transform(image)
                    self.images.append(image)

                    # 클래스 이름을 정수 레이블로 변환하여 labels에 추가
                    label = self.class_label_map[class_name]
                    self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]

        return image, label

