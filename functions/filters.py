#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:35:49 2019

@author: qingchuan-ma
"""
import cv2
from PIL import Image,ImageFilter
import numpy as np

def Blur(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.BLUR)),cv2.COLOR_RGB2BGR)
def Sharpen(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.SHARPEN)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.SHARPEN)), cv2.COLOR_RGB2BGR)
def Smooth(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.SMOOTH)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.SMOOTH)), cv2.COLOR_RGB2BGR)
def Smooth_more(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.SMOOTH_MORE)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.SMOOTH_MORE)), cv2.COLOR_RGB2BGR)
def Emboss(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.EMBOSS)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.EMBOSS)), cv2.COLOR_RGB2BGR)
def Find_edges(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.FIND_EDGES)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.FIND_EDGES)), cv2.COLOR_RGB2BGR)
def Edge_enhance(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.EDGE_ENHANCE)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.EDGE_ENHANCE)), cv2.COLOR_RGB2BGR)
def Edge_enhance_more(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.EDGE_ENHANCE_MORE)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.EDGE_ENHANCE_MORE)), cv2.COLOR_RGB2BGR)
def Contour(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.CONTOUR)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.CONTOUR)), cv2.COLOR_RGB2BGR)
def Detail(ori):
    image = Image.fromarray(cv2.cvtColor(ori, cv2.COLOR_BGR2RGB))
    #return image_ori.filter(ImageFilter.DETAIL)
    return cv2.cvtColor(np.asarray(image.filter(ImageFilter.DETAIL)), cv2.COLOR_RGB2BGR)
def Cartoonise(ori):
    #imgInput_FileName = picture_name
    #imgOutput_FileName = "cartoon" + picture_name
    num_down = 2         #缩减像素采样的数目
    num_bilateral = 7    #定义双边滤波的数目
    #img_rgb = cv2.imread(imgInput_FileName)     #读取图片
    img_rgb= ori
    #用高斯金字塔降低取样
    img_color = img_rgb
#     for _ in range(num_down):
#         img_color = cv2.pyrDown(img_color)
    #重复使用小的双边滤波代替一个大的滤波
    for _ in range(num_bilateral):
        img_color = cv2.bilateralFilter(img_color,d=9,sigmaColor=9,sigmaSpace=7)
    #升采样图片到原始大小
#     for _ in range(num_down):
#         img_color = cv2.pyrUp(img_color)
    #转换为灰度并且使其产生中等的模糊
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 7)
    #检测到边缘并且增强其效果
    img_edge = cv2.adaptiveThreshold(img_blur,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize=9, C=2)
    #转换回彩色图像
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    img_cartoon = cv2.bitwise_and(img_color, img_edge)
    # 保存转换后的图片
    return img_cartoon