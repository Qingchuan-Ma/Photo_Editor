#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:51:19 2019

@author: qingchuan-ma
"""

import numpy as np
import math

def localTranslationWarp(srcImg,startX,startY,endX,endY,radius):
 
    ddradius = float(radius * radius)
    copyImg = np.zeros(srcImg.shape, np.uint8)
    copyImg = srcImg.copy()
    # 计算公式中的|m-c|^2
    ddmc = (endX - startX) * (endX - startX) + (endY - startY) * (endY - startY)
    H, W, C = srcImg.shape
    for i in range(W):
        for j in range(H):
            #计算该点是否在形变圆的范围之内
            #优化，第一步，直接判断是会在（startX,startY)的矩阵框中
            if math.fabs(i-startX)>radius and math.fabs(j-startY)>radius:
                continue
            distance = ( i - startX ) * ( i - startX) + ( j - startY ) * ( j - startY )
            if(distance < ddradius):
                #计算出（i,j）坐标的原坐标
                #计算公式中右边平方号里的部分
                ratio=(  ddradius-distance ) / ( ddradius - distance + ddmc)
                ratio = ratio * ratio
 
                #映射原位置
                UX = i - ratio  * ( endX - startX )
                UY = j - ratio  * ( endY - startY )
 
                #根据双线性插值法得到UX，UY的值
                value = BilinearInsert(srcImg,UX,UY)
                #改变当前 i ，j的值
                copyImg[j,i] =value
 
    return copyImg
 
 
#双线性插值法
def BilinearInsert(src,ux,uy):
    w,h,c = src.shape
    if c == 3:
        x1=int(ux)
        x2=x1+1
        y1=int(uy)
        y2=y1+1

        part1=src[y1,x1].astype(np.float)*(float(x2)-ux)*(float(y2)-uy)
        part2=src[y1,x2].astype(np.float)*(ux-float(x1))*(float(y2)-uy)
        part3=src[y2,x1].astype(np.float) * (float(x2) - ux)*(uy-float(y1))
        part4 = src[y2,x2].astype(np.float) * (ux-float(x1)) * (uy - float(y1))

        insertValue=part1+part2+part3+part4

        return insertValue.astype(np.int8)
 
def nose_thin_auto(src, points, extend):   #  0.5  to 1
    left_point= points[31]
    left_point_down=points[33]

    right_point = points[35]
    right_point_down = points[33]

    endPt = points[33]
 
    r_left=math.sqrt((left_point[0]-left_point_down[0])*(left_point[0]-left_point_down[0])+
                        (left_point[1] - left_point_down[1]) * (left_point[1] - left_point_down[1]))
 
    r_right=math.sqrt((right_point[0]-right_point_down[0])*(right_point[0]-right_point_down[0])+
                        (right_point[1] -right_point_down[1]) * (right_point[1] -right_point_down[1]))
  
    thin_image = localTranslationWarp(src,left_point[0],left_point[1],endPt[0],endPt[1],r_left*extend)
   
    thin_image = localTranslationWarp(thin_image, right_point[0], right_point[1], endPt[0],endPt[1], r_right*extend)
    
    return thin_image