import os
from PIL import Image
import torch
from torchvision.transforms import transforms
from loader import Data
from model import customCNN_v5

def load_test_images(root_dir):
    test_images = []
    for filename in os.listdir(root_dir):
        if filename.endswith(".png"):
            filepath = os.path.join(root_dir, filename)
            image = Image.open(filepath).convert("RGB")
            test_images.append(image)
    return test_images

def predict(model, test_images, class_names):
    predictions = []
    model.eval()
    with torch.no_grad():
        for image in test_images:
            image = data_transform(image).unsqueeze(0)
            output = model(image)
            _, predicted = torch.max(output, 1)
            predicted_class_name = class_names[predicted.item()]
            predictions.append(predicted_class_name)
    return predictions

# 데이터 및 모델 로드
test_images_dir = "./test"
data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])
test_images = load_test_images(test_images_dir)
train_data = Data(root_dir="./train", transform=data_transform)
class_names = train_data.class_names
model = customCNN_v5(num_classes=len(class_names))

# 모델 학습
# 이전에 훈련시킨 코드를 이곳에 넣으세요.

# 테스트 데이터 예측
predicted_classes = predict(model, test_images, class_names)

# 결과 출력
for idx, label in enumerate(predicted_classes):
    print(f"TEST_{idx:03}: {label}")