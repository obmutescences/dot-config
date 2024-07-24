import os
import shutil

# 定义文件路径
click_wav = "click.wav"
cherrymx_blue_dir = "cherrymx-blue"
new_dir = "new-cherrymx-blue"

# 创建新目录，如果不存在则创建
if not os.path.exists(new_dir):
    os.makedirs(new_dir)

# 获取 cherrymx-blue 目录中的文件名
files = os.listdir(cherrymx_blue_dir)

# 遍历文件名并创建新文件
for file_name in files:
    if "-1" in file_name:
        # 构建新文件的完整路径
        new_file_path = os.path.join(new_dir, file_name)
        # 复制 click.wav 文件到新文件
        shutil.copyfile(click_wav, new_file_path)
    else:
        new_file_path = os.path.join(new_dir, file_name)
        shutil.copyfile(cherrymx_blue_dir + "/" + file_name, new_file_path)

print(f"Files copied successfully to {new_dir}")
