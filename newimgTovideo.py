import os
import cv2
import numpy as np

path = 'C:/Users/chenda/Desktop/moveOrvideo_data/img-GI/'
filelist = os.listdir(path)

fps = 24  # 视频每秒24帧
size = (64, 64)  # 需要转为视频的图片的尺寸
# 可以使用cv2.resize()进行修改

video = cv2.VideoWriter("C:/Users/chenda/Desktop/moveOrvideo_data/video/1_GI.avi", cv2.VideoWriter_fourcc('I', '4', '2', '0'),
                        fps, size)
# 视频保存在当前目录下

for i in range(1, len(filelist)+1):
        item = path + str(i) +".jpg"
        # print(item)
        img = cv2.imread(item)
        video.write(img)

video.release()
cv2.destroyAllWindows()
