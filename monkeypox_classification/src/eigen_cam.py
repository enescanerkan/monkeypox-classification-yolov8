import torch
import cv2
import numpy as np
from ultralytics import YOLO
from PIL import Image

# Eğitilmiş YOLOv8 modelini yüklüyorum
model_path = r"C:\Users\Monster\PycharmProjects\pythonProject\monkeypox\models\best.pt"
model = YOLO(model_path)

# Görüntüyü açıyorum
image_path = r"C:\Users\Monster\Desktop\monkeypox-39006_b.jpg"
image = Image.open(image_path)

# Son konvolüsyon katmanının çıktısını almak için hook fonksiyonunu ayarlıyorum
activation = {}
def get_activation(name):
    def hook(model, input, output):
        activation[name] = output.detach()
    return hook

# Son konvolüsyon katmanına hook ekliyorum
model.model.model[-2].register_forward_hook(get_activation('feat_extract'))

# Modeli görüntü üzerinde çalıştırıyorum
results = model(image)

# YOLO çıktısını görselleştiriyorum (RGB formatına çeviriyorum)
yolo_result_image = results[0].plot()

# Son katmandaki aktivasyon haritasını alıyorum
feat_map = activation['feat_extract'][0]

# CAM'i hesaplıyorum (mutlak değer üzerinden ortalama alıyorum)
cam = torch.mean(torch.abs(feat_map), dim=0).cpu().numpy()

# CAM değerlerini normalize ediyorum
cam = (cam - np.min(cam)) / (np.max(cam) - np.min(cam))

# Kontrasta biraz oynama yapıyorum
cam = np.power(cam, 2)

# Isı haritasını oluşturuyorum
heatmap = cv2.applyColorMap(np.uint8(255 * cam), cv2.COLORMAP_JET)

# Isı haritasını orijinal görüntüyle birleştiriyorum
original_image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
heatmap_resized = cv2.resize(heatmap, (original_image.shape[1], original_image.shape[0]))  # Haritayı orijinal boyutlara uyarlıyorum
cam_output = cv2.addWeighted(original_image, 0.6, heatmap_resized, 0.4, 0)

# Sonuçları gösteriyorum (YOLO çıktısı RGB formatında)
cv2.imshow('YOLO Result', yolo_result_image)
cv2.imshow('CAM', cam_output)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Sonuçları kaydediyorum
cv2.imwrite('custom_yolov8_result.jpg', cv2.cvtColor(yolo_result_image, cv2.COLOR_RGB2BGR))
cv2.imwrite('custom_yolov8_cam.jpg', cam_output)
