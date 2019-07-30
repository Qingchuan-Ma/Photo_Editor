#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:33:52 2019

@author: qingchuan-ma
"""
import cv2
from PIL import Image
import numpy as np

def christmas(img,mark,x,y,w,h):
    im = Image.fromarray(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    height = int(w*674/1024)
    mark = mark.resize((w, height))
    layer=Image.new('RGBA', im.size, (0,0,0,0))
    layer.paste(mark, (x,y-height))
    out=Image.composite(layer,im,layer)
    img = cv2.cvtColor(np.asarray(out),cv2.COLOR_RGB2BGR)
    return img

def add_picture(img,mark):
    face_cascade = cv2.CascadeClassifier(r'./libs/haarcascade_frontalface_alt.xml')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取人脸识别数据
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        img = christmas(img, mark, x , y, w, h)
    return img
