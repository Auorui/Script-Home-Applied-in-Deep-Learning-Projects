import os
import shutil

# 源文件夹路径, 目标文件夹路径
source_folder = r""
destination_folder = r""

os.makedirs(source_folder, exist_ok=True)
os.makedirs(destination_folder, exist_ok=True)
files = os.listdir(source_folder)

# 用于存放不同后缀的文件
file_groups = {}
# 遍历源文件夹中的所有文件
for filename in files:
    if os.path.isfile(os.path.join(source_folder, filename)):
        # 获取文件的后缀
        file_extension = filename.split('.')[-1]
        if file_extension not in file_groups:
            file_groups[file_extension] = []

        file_groups[file_extension].append(filename)

# 创建目标文件夹（如果不存在）
os.makedirs(destination_folder, exist_ok=True)

# 遍历不同后缀的文件，将它们分别存放在子文件夹中
for extension, file_list in file_groups.items():
    extension_folder = os.path.join(destination_folder, extension)
    os.makedirs(extension_folder, exist_ok=True)

    for filename in file_list:
        source_path = os.path.join(source_folder, filename)
        destination_path = os.path.join(extension_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved {filename} to {extension}/{filename}")

print("文件移动完成")
