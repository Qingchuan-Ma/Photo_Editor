#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 30 18:58:40 2019

@author: qingchuan-ma
"""

import os
import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
from ui_files.ui_photo_editor import *
from other_windows import aboutWindow, PhotoViewer, CommonHelper, FramelessWindow
import ui_files.resource_rc

from functions.chartlet import *
from functions.changeBack import *
from functions.filters import *
from functions.cheeks import *
from functions.skin import *
from functions.lips import *
from functions.nose import *
from functions.eyes import *    
from functions.pre_handle import *
from functions.rmacne import *
from functions.changeface import *


class myWindow(QtWidgets.QMainWindow):
    def __init__(self, parent = None):
        super(myWindow, self).__init__(parent)
        self.imagePath = ''
        self.initUI()
        
    def initUI(self): 
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.openPhoto)
        self.ui.actionExit.triggered.connect(QtWidgets.qApp.quit)
        self.ui.actionClose.triggered.connect(self.closePhoto)
        self.ui.actionSave_as.triggered.connect(self.saveAs)
        self.ui.actionChangeFace.triggered.connect(self.changeface)
        self.ui.actionAbout.triggered.connect(self.about)
        self.ui.actionBackground.triggered.connect(self.changeBackground)
        self.ui.ok.clicked.connect(self.modifyFace)
        self.ui.rmacne.clicked.connect(self.enRmAcne)
        self.ui.actionFilter1 = QtWidgets.QAction('Blur', self)
        self.ui.actionFilter2 = QtWidgets.QAction('Sharpen', self)
        self.ui.actionFilter3 = QtWidgets.QAction('Smooth', self)
        self.ui.actionFilter4 = QtWidgets.QAction('Smooth_more', self)
        self.ui.actionFilter5 = QtWidgets.QAction('Emboss', self)
        self.ui.actionFilter6 = QtWidgets.QAction('Find_edges', self)
        self.ui.actionFilter7 = QtWidgets.QAction('Edge_enhance', self)
        self.ui.actionFilter8 = QtWidgets.QAction('Edge_enhance_more', self)
        self.ui.actionFilter9 = QtWidgets.QAction('Contour', self)
        self.ui.actionFilter10 = QtWidgets.QAction('Detail', self)
        self.ui.actionFilter11 = QtWidgets.QAction('Cartoonise', self)
        self.ui.menuFilter.addAction(self.ui.actionFilter1)
        self.ui.menuFilter.addAction(self.ui.actionFilter2)
        self.ui.menuFilter.addAction(self.ui.actionFilter3)
        self.ui.menuFilter.addAction(self.ui.actionFilter4)
        self.ui.menuFilter.addAction(self.ui.actionFilter5)
        self.ui.menuFilter.addAction(self.ui.actionFilter6)
        self.ui.menuFilter.addAction(self.ui.actionFilter7)
        self.ui.menuFilter.addAction(self.ui.actionFilter8)
        self.ui.menuFilter.addAction(self.ui.actionFilter9)
        self.ui.menuFilter.addAction(self.ui.actionFilter10)
        self.ui.menuFilter.addAction(self.ui.actionFilter11)
        self.ui.actionFilter0.triggered.connect(self.noneFilter)
        self.ui.actionFilter1.triggered.connect(self.filter1)
        self.ui.actionFilter2.triggered.connect(self.filter2)
        self.ui.actionFilter3.triggered.connect(self.filter3)
        self.ui.actionFilter4.triggered.connect(self.filter4)
        self.ui.actionFilter5.triggered.connect(self.filter5)
        self.ui.actionFilter6.triggered.connect(self.filter6)
        self.ui.actionFilter7.triggered.connect(self.filter7)
        self.ui.actionFilter8.triggered.connect(self.filter8)
        self.ui.actionFilter9.triggered.connect(self.filter9)
        self.ui.actionFilter10.triggered.connect(self.filter10)
        self.ui.actionFilter11.triggered.connect(self.filter11)
        self.ui.actionChartlet.triggered.connect(self.addChartlet)
        self.about = aboutWindow(self)
        self.viewer = PhotoViewer(self)
        self.viewer.photoClicked.connect(self.rmAcne)
        self.mode = 0
        VBlayout = QtWidgets.QVBoxLayout(self.ui.widget)
        VBlayout.addWidget(self.viewer)
    
    
    def rmAcne(self, QPoint):
        r = self.ui.rmacne_slider.value()
        if self.state == 1:
            image_q = qudou(self.processedFaceImageData, QPoint.x(), QPoint.y(), r)
        else:
            image_q = qudou(self.imageData, QPoint.x(), QPoint.y(), r)
        self.updatePhoto(image_q)
        
        
    def updatePhoto(self, image_done):
        height, width,_ = image_done.shape
        cvRGBImg = cv2.cvtColor(image_done, cv2.COLOR_BGR2RGB)
        QImg = QtGui.QImage(cvRGBImg, width, height, 3 * width, QtGui.QImage.Format_RGB888)
        pixmap = QtGui.QPixmap.fromImage(QImg)
        self.viewer.setPhoto(pixmap)
        if self.state == 1:
            self.processedFaceImageData = image_done
        elif self.state == 2:
            self.processedFilterImageData = image_done
        else:
            self.imageData = image_done
        
        
    def enRmAcne(self):
        if self.viewer.hasPhoto():
            if self.mode == 0:
                self.ui.ok.setEnabled(0)
                #self.setCursor(QtCore.Qt.CrossCursor)
                self.mode = 1
                self.viewer.setEnabledClicked(1)
            else:
                self.ui.ok.setEnabled(1)
                #self.setCursor(QtCore.Qt.ArrowCursor)
                self.mode = 0
                self.viewer.setEnabledClicked(0)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')

    def changeface(self):
        if self.viewer.hasPhoto():
            imgPath,_ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget, 'Open Another Photo', './', 'Image Files(*.png *jpg *.bmp)')
            if imgPath and os.path.exists(imgPath):
                picture = cv2.imread(imgPath)
                points2 = key_68_marks(picture)
                output_im = change_face(self.imageData, picture, self.points, points2)
                cv2.imwrite('tmp.jpg', output_im)
                output_im = cv2.imread('tmp.jpg')
                self.imageData = cv2.imread('tmp.jpg')
                os.remove('tmp.jpg')
                self.points = key_68_marks(self.imageData)
                self.updatePhoto(output_im)
                self.state = 0
            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')

        
    def modifyFace(self):
        if self.viewer.hasPhoto():
            self.ui.ok.setEnabled(1)
            eyes_ENLARGE = self.ui.eyes_slider.value()/5
            nose_EXTEND = self.ui.nose_slider.value()/100
            face_EXTEND = self.ui.face_slider.value()/100
            lip_COLOR = self.ui.lip_slider.value()
            mopi_EXTEND = self.ui.mopi_slider.value()
            image_L =  eye_enlarge(self.points, self.imageData, 1+eyes_ENLARGE/100, 0)
            image_LR =  eye_enlarge(self.points, image_L, 1+eyes_ENLARGE/100, 1)
            image_en = nose_thin_auto(image_LR, self.points, nose_EXTEND)
            image_enl = lip_enhance(self.points, image_en, 1.5 , lip_COLOR)
            image_enlf = face_thin_auto(image_enl, self.points, face_EXTEND)
            image_enlfm = beauty_face(image_enlf, mopi_EXTEND)
            self.state = 1
            self.updatePhoto(image_enlfm)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')
        
        
    def changeBackground(self):
        if self.viewer.hasPhoto():
            self.ui.ok.setEnabled(0)
            imgPath,_ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget, 'Open Background Photo', './', 'Image Files(*.png *jpg *.bmp)')
            if imgPath and os.path.exists(imgPath):
                gray_image = cv2.imread(imgPath)
                gray_image = cv2.resize(gray_image, (self.imageData.shape[1],self.imageData.shape[0]), interpolation = cv2.INTER_CUBIC)
                image_back = mask_rcnn_background(self.imageData, gray_image)
                self.state = 0
                self.updatePhoto(image_back)
            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','No photo, Please open a photo first')
    
    def addChartlet(self):
        if self.viewer.hasPhoto():
            self.ui.ok.setEnabled(0)
            imgPath,_ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget, 'Open Chartlet Photo', './', 'Image Files(*.png *jpg *.bmp)')
            if imgPath and os.path.exists(imgPath):
                picture = Image.open(imgPath)
                image_add = add_picture(self.imageData, picture)
                self.state = 0
                self.updatePhoto(image_add)
            else:
                pass
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','No photo, Please open a photo first')
        
    def about(self):
        self.about.show()

    def saveAs(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                image_write = self.processedFaceImageData
            elif self.state == 2:
                image_write = self.processedFilterImageData
            else:
                image_write = self.imageData
            imgPath, _ = QtWidgets.QFileDialog.getSaveFileName(self.ui.centralwidget,'Save Photo File','./','Image Files(*.png *.jpg *.bmp)')
            cv2.imwrite(imgPath, image_write)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','No photo, please open a photo first')
    
    
    def openPhoto(self):
        self.imagePath, _ = QtWidgets.QFileDialog.getOpenFileName(self.ui.centralwidget,'Open Photo File','./','Image Files(*.png *.jpg *.bmp)')#;;Text Files (*.txt)')
        if self.imagePath and os.path.exists(self.imagePath):
            self.ui.ok.setEnabled(1)
            self.viewer.setPhoto(QtGui.QPixmap(self.imagePath))
            self.imageData = cv2.imread(self.imagePath)
            self.points = key_68_marks(self.imageData)     # get points
            self.processedFaceImageData = cv2.imread(self.imagePath)
            self.processedFilterImageData = cv2.imread(self.imagePath)
        else:
            pass

    def closePhoto(self):
        self.ui.ok.setEnabled(1)
        self.viewer.setPhoto()


    def noneFilter(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = self.imageData
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
    
    def filter1(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Blur(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter2(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Sharpen(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter3(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Smooth(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter4(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Smooth_more(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter5(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Emboss(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter6(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Find_edges(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter7(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Edge_enhance(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter8(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Edge_enhance_more(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter9(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Contour(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter10(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Detail(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
            
    def filter11(self):
        if self.viewer.hasPhoto():
            if self.state == 1:
                self.imageData = self.processedFaceImageData
                self.ui.ok.setEnabled(0)
            else:
                pass
            self.state = 2
            image_filter = Cartoonise(self.imageData)
            self.updatePhoto(image_filter)
        else:
            QtWidgets.QMessageBox.warning(self.ui.centralwidget,'Error','Please open a photo first')    
    

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    qssStyle = CommonHelper.readQss('./ui_files/style.qss')
    mainWnd = FramelessWindow()
    mainWnd.setFrameSize(600,400)
    mainWnd.setWindowTitle('Photo Editor')
    mainWnd.setStyleSheet(qssStyle)
    mainWnd.setWindowIcon(QtGui.QIcon('./ui_files/source/246px-Adobe_Photoshop_CC_icon.png'))
    mainWnd.setWidget(myWindow(mainWnd))  # 把自己的窗口添加进来
    mainWnd.show()
    sys.exit(app.exec_())