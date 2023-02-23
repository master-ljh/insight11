import cv2

# 读取视频文件
video_path = 'datasets/videos/tumor/tumor_08.mp4'
cap = cv2.VideoCapture(video_path)

# 设置保存图像的路径和文件名前缀
save_dir = 'output/tumor/'
prefix = 'tumor_08'

# 定义帧数计数器
frame_count = 0

# 循环读取视频帧
while True:
    # 读取视频帧
    ret, frame = cap.read()

    # 判断是否读取到帧
    if not ret:
        break

    # 保存图像文件
    frame_count += 1
    file_name = save_dir + prefix + str(frame_count).zfill(5) + '.jpg'
    cv2.imwrite(file_name, frame)

# 释放资源
cap.release()

