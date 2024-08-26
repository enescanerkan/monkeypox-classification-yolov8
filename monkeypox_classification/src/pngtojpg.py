from PIL import Image
import os

def convert_bmp_to_jpg(folder_path):
    # Belirtilen klasördeki tüm dosyaları alma
    file_list = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Her dosya için döndürme
    for file_name in file_list:
        # Dosyanın uzantısını kontrol etme ve .bmp ise dönüştürme
        if file_name.lower().endswith(".bmp"):
            bmp_path = os.path.join(folder_path, file_name)
            jpg_path = os.path.join(folder_path, os.path.splitext(file_name)[0] + ".jpg")

            # BMP dosyasını aç ve JPG olarak kaydetme
            with Image.open(bmp_path) as img:
                img.convert("RGB").save(jpg_path, "JPEG")

            # BMP dosyasını silmek
            os.remove(bmp_path)

if __name__ == "__main__":
    folder_path = r"C:\Users\Monster\Desktop\data\none\val" # Klasör yolunu güncelleme
    convert_bmp_to_jpg(folder_path)