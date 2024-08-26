import os
import cv2
from tqdm import tqdm


def augment_images(original_images_folder, output_folder):
    original_images = os.listdir(original_images_folder)

    output_images_folder = os.path.join(output_folder, "images")
    os.makedirs(output_images_folder, exist_ok=True)

    for image_name in tqdm(original_images, desc="İşleniyor"):
        image_path = os.path.join(original_images_folder, image_name)
        original_image = cv2.imread(image_path)

        # Çoğaltılmamış fotoğrafları kaydet
        output_image_path = os.path.join(output_images_folder, f"{os.path.splitext(image_name)[0]}.bmp")
        cv2.imwrite(output_image_path, original_image)

        # Yatay çevirme işlemi
        flipped_image = cv2.flip(original_image, 1)
        output_image_path = os.path.join(output_images_folder, f"{os.path.splitext(image_name)[0]}_flipped.bmp")
        cv2.imwrite(output_image_path, flipped_image)

        # Dikey çevirme işlemi
        flipped_image = cv2.flip(original_image, 0)
        output_image_path = os.path.join(output_images_folder,
                                         f"{os.path.splitext(image_name)[0]}_flipped_vertical.bmp")
        cv2.imwrite(output_image_path, flipped_image)

        # Dikey ve Yatay çevirme birleşik (Önce dikey, sonra yatay)
        flipped_image = cv2.flip(original_image, 0)
        flipped_image = cv2.flip(flipped_image, 1)
        output_image_path = os.path.join(output_images_folder,
                                         f"{os.path.splitext(image_name)[0]}_flipped_vertical_horizontal.bmp")
        cv2.imwrite(output_image_path, flipped_image)


if __name__ == "__main__":
    original_images_folder = r"C:\Users\Monster\Desktop\data\none"
    output_folder_augmented = r"C:\Users\Monster\Desktop\augment_data\augment_none"

    augment_images(original_images_folder, output_folder_augmented)
