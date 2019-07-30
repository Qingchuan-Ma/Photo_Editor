#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:47:16 2019

@author: qingchuan-ma
"""
import numpy as np
import cv2
from PIL import Image,ImageFilter

def lip_enhance(points,image_RGB,ENHANCE,CHANGE):  
    
    if CHANGE == 255:
        return image_RGB
    
    region = []
    region = points[48:60]
    image_RGBA=Image.fromarray(image_RGB, mode='RGB')
    image_RGBA=image_RGBA.convert(mode='RGBA')
    
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

    RATIO=0.9
    rect_YH=Mask_Leye_YH.crop(box=(x_indeces[0],y_indeces[0],x_indeces[-1],y_indeces[-1]))
    rect_YH=rect_YH.resize((int(RATIO*x_len),int(RATIO*y_len)))

    LEFT=int(x_cent-RATIO*x_len/2)
    #RIGHT=int(x_cent+RATIO*x_len/2)
    TOP=int(y_cent-RATIO*y_len/2)
    #BOTTOM=int(y_cent+RATIO*y_len/2)

    mask_empty=Image.fromarray(empty,mode='L')
    mask_new=mask_empty.copy()
    mask_new.paste(rect_YH,(LEFT,TOP))
    mask_leye=mask_new

    rect_Leye=image_RGBA.convert(mode='HSV')
    
#    ENHANCE=2
    rect_leye=np.asarray(rect_Leye)
    temp1=rect_leye[:,:,1]
    temp1=temp1*ENHANCE
    temp0=rect_leye[:,:,0]
    temp0=(temp0+CHANGE)%256
    rect=rect_leye.copy()
    rect[:,:,1]=temp1
    rect[:,:,0]=temp0
    LIP=Image.fromarray(rect,mode='HSV')
    lip=LIP.convert(mode='RGBA')
    lip.putalpha(mask_leye)
    
    image_L=image_RGBA.copy()
    image_L.alpha_composite(lip,dest=(0,0))
    image_L_RGB = image_L.convert(mode='RGB')
    
    return np.asarray(image_L_RGB)