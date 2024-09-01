import torch
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image
import os

# Eğitilmiş YOLOv8 modelini yüklüyorum
model_path = r"C:\Users\Monster\PycharmProjects\pythonProject\monkeypox\models\best.pt"
model = YOLO(model_path)

# Görüntülerin bulunduğu klasör
image_folder = r"C:\Users\Monster\Desktop\YOLOv8_Layers_Images"

# Çıktıların kaydedileceği klasör
output_folder = r"C:\Users\Monster\Desktop\kumas_output"
os.makedirs(output_folder, exist_ok=True)

# Aktivasyon sözlüğü
activation = {}


# Aktivasyonları almak için hook fonksiyonu
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()

    return hook


# Tüm katmanlara hook ekliyoruz
for i in range(len(model.model.model)):
    layer_name = f'model.{i}'
    model.model.model[i].register_forward_hook(get_activation(layer_name))


# Özellik haritasını işleme fonksiyonu
def process_feature_map(feature_map):
    # Tensor boyutlarını kontrol et
    if len(feature_map.shape) == 4:  # (batch, channels, height, width)
        feature_map = feature_map.squeeze(0)  # Batch boyutunu kaldır
        feature_map = torch.mean(feature_map, dim=0)  # Kanallar üzerinden ortalama al
    elif len(feature_map.shape) == 2:  # Fully connected layer çıktısı
        feature_map = feature_map.squeeze(0)  # Batch boyutunu kaldır
        size = int(np.sqrt(feature_map.shape[0]))
        feature_map = feature_map.view(size, size)
    elif len(feature_map.shape) == 3:  # (channels, height, width)
        feature_map = torch.mean(feature_map, dim=0)  # Kanallar üzerinden ortalama al

    # NumPy array'e çevir ve normalize et
    feature_map = feature_map.cpu().numpy()
    feature_map = (feature_map - feature_map.min()) / (feature_map.max() - feature_map.min() + 1e-8)
    return (feature_map * 255).astype(np.uint8)


# Klasördeki tüm .png ve .jpg dosyaları için işlem yapıyoruz
for image_name in os.listdir(image_folder):
    if image_name.endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(image_folder, image_name)
        image = Image.open(image_path)

        # Orijinal görüntüyü BGR formatına çeviriyoruz (OpenCV için)
        original_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

        # Modeli görüntü üzerinde çalıştırıyoruz
        results = model(image)

        # Tüm katmanlar için özellik haritalarını kaydediyoruz
        for layer_name, feature_map in activation.items():
            try:
                processed_map = process_feature_map(feature_map)
                if processed_map is not None and processed_map.size > 0:
                    resized_map = cv2.resize(processed_map, (image.size[0], image.size[1]))

                    # Görüntüleri kaydediyoruz
                    base_name = os.path.splitext(image_name)[0]
                    output_path = os.path.join(output_folder, f'{base_name}_{layer_name}.png')
                    cv2.imwrite(output_path, resized_map)
                    print(f"Kaydedildi: {output_path}")
            except Exception as e:
                print(f"Hata oluştu {layer_name} işlenirken: {str(e)}")

        # Orijinal görüntüyü kaydediyoruz
        base_name = os.path.splitext(image_name)[0]
        cv2.imwrite(os.path.join(output_folder, f'{base_name}_original.png'), original_image)

        print(f"İşlem tamamlandı: {image_name}")

print("Tüm görüntüler işlendi ve kaydedildi.")