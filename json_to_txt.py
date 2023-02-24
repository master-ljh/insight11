import os
import json

# 源文件夹和目标文件夹路径
source_folder = "tumor_json"
target_folder = "tumor_txt"

# 遍历源文件夹中的所有文件
for filename in os.listdir(source_folder):
    # 如果文件名以 .json 结尾，则表示这是一个 JSON 文件
    if filename.endswith(".json"):
        # 拼接源文件的完整路径
        source_path = os.path.join(source_folder, filename)
        # 构造目标文件的完整路径，将 .json 后缀替换为 .txt 后缀
        target_path = os.path.join(target_folder, filename[:-5] + ".txt")
        
        # 读取 JSON 文件并将其转换为字符串
        with open(source_path) as f:
            json_data = json.load(f)
            txt_data = json.dumps(json_data)
        
        # 将字符串写入目标文件
        with open(target_path, "w") as f:
            f.write(txt_data)
