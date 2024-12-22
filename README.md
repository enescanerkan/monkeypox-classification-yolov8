# Monkeypox Detection

**Author**: Enes Can Erkan  
**Date**: 26.08.2024

## Description
This project, named **"Monkeypox Detection,"** focuses on detecting monkeypox lesions using a YOLOv8 model. The project includes training the model with two classes (**monkeypox**, **none**) using datasets collected from web scraping and Kaggle. The images were augmented fourfold before training to improve model performance. Eigen-CAM was used to visualize the model's predictions.

*(Bu proje, "Monkeypox Detection" olarak adlandırılmış olup, maymun çiçeği lezyonlarını YOLOv8 modeli kullanarak tespit etmeye odaklanmaktadır. Model, web scraping ve Kaggle'dan toplanan veri setleriyle eğitilmiş olup, iki sınıf (monkeypox, none) içermektedir. Görüntüler, model performansını artırmak amacıyla eğitim öncesinde dört kat artırılmıştır. Modelin tahmin sonuçlarını görselleştirmek için Eigen-CAM kullanılmıştır.)*

## Features
- **Monkeypox Detection**: Detects monkeypox lesions in images using a custom-trained YOLOv8 model.  
  *(Maymun çiçeği tespiti: Özel olarak eğitilmiş YOLOv8 modeli kullanarak görüntülerde maymun çiçeği lezyonlarını tespit eder.)*

- **Data Augmentation**: The dataset was augmented four times to enhance the model’s ability to generalize.  
  *(Veri Çoğaltma: Veri seti, modelin genelleme yeteneğini artırmak için dört kat artırılmıştır.)*

- **Eigen-CAM Visualization**: Visualizes model predictions using Eigen-CAM, helping interpret the model's focus areas.  
  *(Eigen-CAM Görselleştirme: Modelin odaklandığı alanları yorumlamak için Eigen-CAM kullanılarak model tahminleri görselleştirilmiştir.)*

- **Training Results**: The training weights are saved as `best.pt` and `last.pt`, and predictions are stored in the `tested_images` directory.  
  *(Eğitim Sonuçları: Eğitim ağırlıkları `best.pt` ve `last.pt` olarak kaydedilmiştir, tahmin sonuçları ise `tested_images` dizininde saklanmaktadır.)*

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/enescanerkan/monkeypox_classification_YOLOv8.git
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Usage
1. Place the images you want to test in the `data/test/monkeypox` directory.  
   *(İşlemek istediğiniz görüntüleri `data/test/monkeypox` dizinine yerleştirin.)*

2. Update the paths in `main.py` according to your image locations.  
   *(Görüntü konumlarını `main.py` dosyasında güncelleyin.)*

3. Run the `main.py` script to start the prediction process:

    ```bash
    python main.py
    ```

4. The predicted images and corresponding Eigen-CAM visualizations will be saved in the `tested_images` and `eigen_cam_images` directories, respectively.  
   *(Tahmin edilen görüntüler ve ilgili Eigen-CAM görselleştirmeleri sırasıyla `tested_images` ve `eigen_cam_images` dizinlerine kaydedilecektir.)*

## File Descriptions
- **main.py**: The main script for running the model and visualizing predictions.  
  *(Ana script, modeli çalıştırmak ve tahminleri görselleştirmek için.)*

- **yolo_model.py**: Contains functions related to loading and running the YOLOv8 model.  
  *(YOLOv8 modelini yükleme ve çalıştırma ile ilgili fonksiyonları içerir.)*

- **eigen_cam.py**: Responsible for generating Eigen-CAM visualizations.  
  *(Eigen-CAM görselleştirmeleri oluşturmakla sorumludur.)*

- **image_processing.py**: Contains helper functions for image preprocessing.  
  *(Görüntü ön işleme için yardımcı fonksiyonları içerir.)*
## Test Images
![monkey_pox(6)](https://github.com/user-attachments/assets/7796ccad-ccc3-4da9-9209-ac84514a0e97)

![monkey_pox(5)](https://github.com/user-attachments/assets/40a19634-5d6e-41b1-9562-9b9b26b6b686)

## Synthetic Data Test Images

<table>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/7ecfab8d-3466-492d-bc7a-145c6b90d02e" alt="mpox_18_cam" width="300">
      <img src="https://github.com/user-attachments/assets/5dabb251-4931-4f49-8558-760442fd11cd" alt="mpox_18_yolo" width="300">
      <img src="https://github.com/user-attachments/assets/5b638516-c9e7-40f3-8331-d683df401092" alt="mpox_18_original" width="300">
    </td>
  </tr>
  <tr>
    <td>
      <img src="https://github.com/user-attachments/assets/d9b9c5de-30c1-402a-bcf1-00a1da6ce5fe" alt="mpox_46_cam" width="300">
      <img src="https://github.com/user-attachments/assets/01bb4e71-5bda-4692-a939-219736ffd324" alt="mpox_46_yolo" width="300">
      <img src="https://github.com/user-attachments/assets/adaf5b84-d34c-4b57-8937-4b07a89f491a" alt="mpox_46_original" width="300">
    </td>
  </tr>
</table>



## Contributing
Feel free to submit pull requests or issues if you find any bugs or have suggestions for improvements.  
*(Bir hata bulursanız veya geliştirme önerileriniz varsa, çekme istekleri veya sorunlar göndermekten çekinmeyin.)*

## License
This project is licensed under the MIT License.  
*(Bu proje MIT Lisansı altında lisanslanmıştır.)*




