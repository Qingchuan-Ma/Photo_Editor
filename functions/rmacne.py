import numpy as np
import cv2

'''
传入cv2打开的图片，鼠标点击得到的坐标，祛痘半径
'''
def qudou(img, x, y, r = 80):
    value = 20
    temp = cv2.bilateralFilter(img, value, value * 2, value / 2)
    img_size = img.shape
    circle_dot = (x, y)

    for i in range(img_size[0]):
        for j in range(img_size[1]):
            if (i - circle_dot[1])**2 + (j - circle_dot[0])**2 < r**2:
                img[i][j] = temp[i][j]
    return img
    