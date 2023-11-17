from PIL import Image
import os


def resize_images(input_folder, output_folder, target_size):
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            with Image.open(input_path) as img:
                resized_img = img.resize(target_size, Image.ANTIALIAS)
                resized_img.save(output_path)
                print(f"Resized {filename} successfully.")


input_folder_path = "D:\PythonProject\YOLO\yolo5\img\dataimg"
output_folder_path = "D:\PythonProject\YOLO\yolo5\img\JPEGImages"
target_size = (864, 640)

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

resize_images(input_folder_path, output_folder_path, target_size)
