
import os
from PIL import Image
from torch.utils.data import Dataset
import torchvision.transforms as transforms

class CustomDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.images = []
        self.labels = []
        self.class_names = []
        self.class_label_map = {}
        label_index = 0

        for root, dirs, files in os.walk(root_dir):
            for filename in files:
                if filename.endswith(".png"):
                    filepath = os.path.join(root, filename)
                    class_name = os.path.basename(root)

                    if class_name not in self.class_label_map:
                        self.class_label_map[class_name] = label_index
                        self.class_names.append(class_name)
                        label_index += 1

                    image = Image.open(filepath).convert("RGB")
                    if self.transform:
                        image = self.transform(image)
                    self.images.append(image)
                    label = self.class_label_map[class_name]
                    self.labels.append(label)

    def __len__(self):
        return len(self.images)

    def __getitem__(self, idx):
        image = self.images[idx]
        label = self.labels[idx]
        return image, label

data_transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
])


