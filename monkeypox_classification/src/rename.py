import os
from tqdm import tqdm

def rename_images_in_folder(folder_path, start_num, end_num):
    # Belirtilen klasördeki tüm dosyaları al ve sıralama yap
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    image_files.sort()  # İsimlendirme sırası için dosyaları sıralama

    image_counter = start_num  # Başlangıç numarasını belirle

    for image_name in tqdm(image_files, desc="İsimler Değiştiriliyor"):
        if image_counter > end_num:
            break  # Bitiş numarasına ulaşıldığında durdur

        # Dosya yollarını oluştur
        old_image_path = os.path.join(folder_path, image_name)
        new_image_path = os.path.join(folder_path, f"{image_counter}.bmp")

        # Dosyayı yeniden adlandır
        os.rename(old_image_path, new_image_path)

        image_counter += 1  # Sayacı artır

if __name__ == "__main__":
    folder_path = r"C:\Users\Monster\Desktop\augment_data\augment_none\images" # Klasör yolunu güncelle
    start_num = 1129  # Başlangıç numarası
    end_num = 2258 # Bitiş numarası

    rename_images_in_folder(folder_path, start_num, end_num)
