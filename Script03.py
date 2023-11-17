import cv2
import os

def convert_images(input_folder, output_folder, output_format):
    # 遍历输入文件夹中的所有图像文件
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)

        if os.path.isfile(input_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            img = cv2.imread(input_path)
            output_filename = os.path.splitext(filename)[0] + '.' + output_format.lower()
            output_path = os.path.join(output_folder, output_filename)
            cv2.imwrite(output_path, img)
            print(f"成功将 {filename} 转换为 {output_format} 格式。")

input_folder_path = r""  # 目标路径
output_folder_path = r""  # 存放的路径
target_format = "jpeg"   # 经过测试png,jpg,jpeg,bmp都没问题

if not os.path.exists(output_folder_path):
    os.makedirs(output_folder_path)

convert_images(input_folder_path, output_folder_path, target_format)
