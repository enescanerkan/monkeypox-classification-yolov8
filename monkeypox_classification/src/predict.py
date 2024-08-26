import cv2
import numpy as np
from ultralytics import YOLO

# Model yükleme
model_path = r"C:\Users\Monster\PycharmProjects\pythonProject\monkeypox\models\best.pt"
model = YOLO(model_path)
print("Model yüklendi:", model)

# Görüntü yükleme
image_path = r"C:\Users\Monster\Desktop\Monkeypox-Image-1.webp"
im0 = cv2.imread(image_path)
if im0 is None:
    print("Hata: Görüntü dosyası okunamıyor.")
    exit()

print("Görüntü şekli:", im0.shape)

# Tahmin yapma
results = model.predict(im0)
print("Tahmin sonuçları:", results)

# Sınıflandırma sonucunu görüntü üzerine yazma
if len(results) > 0 and results[0].probs is not None:
    # En yüksek olasılıklı sınıfı al
    class_id = results[0].probs.top1
    class_name = results[0].names[class_id]
    confidence = results[0].probs.top1conf.item()

    # Sonucu görüntü üzerine yaz
    text = f"{class_name}: {confidence:.2f}"
    cv2.putText(im0, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    print(f"Sınıflandırma sonucu: {text}")
else:
    print("Sınıflandırma yapılamadı.")

# Sonucu kaydetme
output_path = "classification_output.png"
cv2.imwrite(output_path, im0)
print(f"Sonuç kaydedildi: {output_path}")