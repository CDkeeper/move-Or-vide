import cv2
import os
#import dlib
import numpy as np

video = "http://admin:admin@172.20.78.218:8081/"
cap = cv2.VideoCapture(video)

step = 0

while True:
    success, img = cap.read()
    cv2.imshow("oridinal_video", img)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#img:{ndarray:(480,640)}
    #print(img.shape)
    img = cv2.resize(img, dsize=(128, 128))
    iteration = 1000
    Sum_of_B = 0
    Sum_of_I = np.zeros(img.shape)
    Sum_of_BI = np.zeros(img.shape)
    for it in range(iteration):
        # if (it + 1) % 1000 ==0:
        #     print('Completion: {:.2%}'.format((it + 1)/iteration))
        I = np.random.normal(0, 1, img.shape)
        Sum_of_I = Sum_of_I + I
        I_img = np.multiply(I, img)
        B = sum(sum(I_img))
        Sum_of_B = Sum_of_B + B
        Sum_of_BI = Sum_of_BI + B * I

    Ave_B = Sum_of_B / iteration  # 桶测量值的均值
    Ave_I = Sum_of_I / iteration  # 热光矩阵的均值
    Ave_BI = Sum_of_BI / iteration  # B*I矩阵的均值
    # 归一化计算鬼成像
    GI = Ave_BI - Ave_I * Ave_B
    mi = np.min(GI)
    mx = np.max(GI)
    GI = 255 * (GI - mi) / (mx - mi)

    step += 1
    # cv2.imshow("GI_video", GI)
    cv2.imwrite("./Video_GI/{}.bmp".format(step), GI)  # img

    #关闭摄像头
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
