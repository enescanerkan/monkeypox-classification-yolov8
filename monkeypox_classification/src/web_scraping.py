from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from PIL import Image
import requests
import io
import os
from datetime import datetime
import time
import random


class ImageDownloader:
    def __init__(self):
        """
        ImageDownloader sınıfını başlatır.
        """
        self.base_dir = os.path.join(os.getcwd(), 'downloaded_images')

    def create_save_directory(self, query):
        """
        İndirilen resimleri kaydetmek için bir dizin oluşturur.

        :param query: Dizin adını oluşturmak için kullanılan arama sorgusu
        :return: Oluşturulan dizinin yolu
        """
        if not os.path.exists(self.base_dir):
            os.makedirs(self.base_dir)

        now = datetime.now()
        sub_dir = f"{query.replace(' ', '_')}_{now.strftime('%Y%m%d_%H%M%S')}"
        save_dir = os.path.join(self.base_dir, sub_dir)
        os.makedirs(save_dir)

        return save_dir

    def search_images(self, query, num_images):
        """
        Bing görsel arama kullanarak resim arar.

        :param query: Arama sorgusu
        :param num_images: Aranacak resim sayısı
        :return: Resim URL'lerinin listesi
        """
        service = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        driver = webdriver.Chrome(service=service, options=options)

        url = f"https://www.bing.com/images/search?q={query}&first=1&tsc=ImageBasicHover"
        driver.get(url)

        image_urls = set()
        scroll_count = 0
        max_scrolls = 10

        while len(image_urls) < num_images and scroll_count < max_scrolls:
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(random.uniform(2, 4))  # Rastgele bekleme süresi

            try:
                thumbnails = driver.find_elements(By.CSS_SELECTOR, "img.mimg")
                for img in thumbnails:
                    if len(image_urls) >= num_images:
                        break
                    src = img.get_attribute('src')
                    if src and not src.startswith('data:') and not src.endswith('favicon.ico'):
                        image_urls.add(src)

                scroll_count += 1
                print(f"Kaydırma {scroll_count}: {len(image_urls)} resim URL'si bulundu.")
            except Exception as e:
                print(f"Bir hata oluştu: {e}")

        driver.quit()
        return list(image_urls)[:num_images]

    def download_image(self, url, save_path):
        """
        Verilen URL'den bir resim indirir ve belirtilen yola kaydeder.

        :param url: İndirilecek resmin URL'si
        :param save_path: Resmin kaydedileceği yol
        :return: İndirme başarılı ise True, değilse False
        """
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
            response = requests.get(url, headers=headers, timeout=10)
            img = Image.open(io.BytesIO(response.content))

            save_path = save_path.rsplit('.', 1)[0] + '.png'
            img.save(save_path, format='PNG')
            return True
        except Exception as e:
            print(f"Hata: {url} indirilirken bir sorun oluştu: {e}")
            return False

    def run(self):
        """
        Resim indirme işlemini çalıştırır.

        :return: None
        """
        query = input("Arama terimini girin: ")
        num_images = int(input("Kaç resim indirmek istiyorsunuz? "))

        save_directory = self.create_save_directory(query)
        image_urls = self.search_images(query, num_images)

        print(f"Toplam {len(image_urls)} resim URL'si bulundu.")
        print(f"İstenen {num_images} resmi indirmeye başlıyorum...")

        downloaded_count = 0
        for i, url in enumerate(image_urls):
            save_path = os.path.join(save_directory, f"image_{i + 1}.png")
            if self.download_image(url, save_path):
                downloaded_count += 1
                print(f"{downloaded_count}. resim indirildi: {save_path}")

        print(f"\nİşlem tamamlandı. {downloaded_count} resim '{save_directory}' klasörüne kaydedildi.")