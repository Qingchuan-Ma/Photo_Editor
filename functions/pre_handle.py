#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:56:03 2019

@author: qingchuan-ma
"""

import dlib

def key_68_marks(img):
    detector = dlib.get_frontal_face_detector()
    faces = detector(img, 1)
    print(faces)
    landmark_predictor = dlib.shape_predictor(r'./libs/shape_predictor_68_face_landmarks.dat')
    points = []
    if (len (faces) > 0):
        for k, d in enumerate(faces):
            #cv2.rectangle(img, (d.left(), d.top()), (d.right(), d.bottom()), (255, 0, 0))
            shape = landmark_predictor(img, d)
            for i in range(68):
                num = str(shape.part(i))[1:-1].split(",")
                points.append([int(num[0]), int(num[1])])
    return points