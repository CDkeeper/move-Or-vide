import numpy as np  # 不用管
import cv2 as cv  # 不用管
from PIL import Image

for i in range(1, 1562):  # range(1, 60001) = 1~60000
    imgpath = "C:/Users/chenda/Desktop/moveOrvideo_data/imgByvideo/{}.jpg".format(i)  # 图片路径
    # img_PIL = Image.open(imgpath)
    # img_array = np.array(img_PIL)
    # print(type(img_array))
    # print(img_array.shape)
    img = cv.imread(imgpath, 0)  # 读取图片，0代表灰白图片

    iteration = 1000  # 设定帧数，10000帧

    Sum_of_B = 0  # 定义桶测量值的和
    Sum_of_I = np.zeros(img.shape)  # 定义热光矩阵的和
    Sum_of_BI = np.zeros(img.shape)  # 定义B*I矩阵的和

    for it in range(iteration):
        # 进度提示语句，不用管
        if (it + 1) % 1000 == 0:
            print('Completion: {:.2%}'.format((it + 1) / iteration))

        I = np.random.normal(0, 1, img.shape)  # 生成热光矩阵
        Sum_of_I = Sum_of_I + I  # 热光矩阵累加

        I_img = np.multiply(I, img)  # 热光矩阵乘以图像矩阵，即模拟热光照射物体的过程，I_img即为照射物体后的光束矩阵
        B = sum(sum(I_img))  # 对照射物体后的光束矩阵求和，即获得桶测量值 B = sum(sum(I_img))

        Sum_of_B = Sum_of_B + B  # 桶测量值累加
        Sum_of_BI = Sum_of_BI + B * I  # B*I矩阵累加

    Ave_B = Sum_of_B / iteration  # 桶测量值的均值
    Ave_I = Sum_of_I / iteration  # 热光矩阵的均值
    Ave_BI = Sum_of_BI / iteration  # B*I矩阵的均值
    GI = Ave_BI - Ave_I * Ave_B  # 计算鬼成像
    # print(np.shape(Ave_BI))
    # print(np.shape(GI))
    mi = np.min(GI)
    mx = np.max(GI)
    GI = 255 * (GI - mi) / (mx - mi)

    cv.imwrite("C:/Users/chenda/Desktop/moveOrvideo_data/img-GI/{}.jpg".format(i), GI)  # 导出图片
print("Completed!")
