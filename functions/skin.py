#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:07 2019

@author: qingchuan-ma
"""

import numpy as np
import cv2

def beauty_face(img, degree = 5, detail = 1):
    if degree >= 1:
            
        dst = np.zeros_like(img)
        #int value1 = 3, value2 = 1; 磨皮程度与细节程度的确定
        value = 5
        v1 = int(degree)
        v2 = int(detail)
        dx = v1 * 5 # 双边滤波参数之一 
        fc = v1 * 12.5 # 双边滤波参数之一 
        p = 0.1
       
        temp4 = np.zeros_like(img)
        
        temp1 = cv2.bilateralFilter(img,dx,fc,fc)
        temp2 = cv2.subtract(temp1,img);
        temp2 = cv2.add(temp2,(10,10,10,128))
        temp3 = cv2.GaussianBlur(temp2,(2*v2 - 1,2*v2-1),0)
        temp4 = cv2.add(img,temp3)
        dst = cv2.addWeighted(img,p,temp4,1-p,0.0)
        dst = cv2.add(dst,(10, 10, 10,255))
        dst = cv2.bilateralFilter(dst, value, value * 2, value / 2)
    #cv2.imwrite("4.jpg",dst)
    else:
        dst = img
    return dst
