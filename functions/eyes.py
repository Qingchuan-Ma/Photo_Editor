#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:53:25 2019

@author: qingchuan-ma
"""
from PIL import Image, ImageFilter
import numpy as np
import cv2


def eye_enlarge(points,image_RGB,ENLARGE, ctrl):   #0 - 20
    region=[]
    
    image_RGBA=Image.fromarray(image_RGB, mode='RGB')
    image_RGBA=image_RGBA.convert(mode='RGBA')
    if ctrl == 0 :
        region = points[36:42]
    elif ctrl == 1:
        region = points[42:48]
    pixels=np.asarray(image_RGBA)
    
    Leye=cv2.convexHull(np.array(region))
    empty=np.zeros(np.shape(pixels)[:2],dtype='uint8')
    leye=np.array(empty)
    mask_Leye=cv2.fillConvexPoly(leye, Leye,color=256)

    Mask_Leye=Image.fromarray(mask_Leye,mode='L')
    Mask_Leye_YH=Mask_Leye.filter(ImageFilter.GaussianBlur(radius=5))

    mask_pixels=np.asarray(Mask_Leye_YH)
    x_indeces=[j for j in range(pixels.shape[1]) if mask_pixels[:,j].sum() != 0]
    y_indeces=[i for i in range(pixels.shape[0]) if mask_pixels[i].sum() != 0]
    x_cent=int(np.average(x_indeces))
    y_cent=int(np.average(y_indeces))
    x_len=len(x_indeces)
    y_len=len(y_indeces)

    RATIO=2
    rect_YH=Mask_Leye_YH.crop(box=(x_indeces[0],y_indeces[0],x_indeces[-1],y_indeces[-1]))
    rect_YH=rect_YH.resize((int(RATIO*x_len),int(RATIO*y_len)))

    LEFT=int(x_cent-RATIO*x_len/2)
    RIGHT=int(x_cent+RATIO*x_len/2)
    TOP=int(y_cent-RATIO*y_len/2)
    BOTTOM=int(y_cent+RATIO*y_len/2)

    mask_empty=Image.fromarray(empty,mode='L')
    mask_new=mask_empty.copy()
    mask_new.paste(rect_YH,(LEFT,TOP))
    mask_leye=mask_new

    image_Leye=image_RGBA.copy()
    image_Leye.putalpha(mask_leye)

#    ENLARGE=1.15
    #mask_new_pixels=np.asarray(mask_new)
    x_indeces=[j for j in range(pixels.shape[1]) if mask_pixels[:,j].sum() != 0]
    y_indeces=[i for i in range(pixels.shape[0]) if mask_pixels[i].sum() != 0]
    x_cent=int(np.average(x_indeces))
    y_cent=int(np.average(y_indeces))
    x_len=len(x_indeces)
    y_len=len(y_indeces)
    LEFT=int(x_cent-ENLARGE*x_len/2)
    #RIGHT=int(x_cent+ENLARGE*x_len/2)
    TOP=int(y_cent-ENLARGE*y_len/2)
    #BOTTOM=int(y_cent+ENLARGE*y_len/2)

    image_L=image_RGBA.copy()
    rect_Leye=image_Leye.crop(box=(x_indeces[0],y_indeces[0],x_indeces[-1],y_indeces[-1]))
    image_L.alpha_composite(rect_Leye.resize(((int(ENLARGE*x_len),int(ENLARGE*y_len)))),dest=(LEFT,TOP))
    image_L_RGB = image_L.convert(mode='RGB')
    
    return np.asarray(image_L_RGB)
