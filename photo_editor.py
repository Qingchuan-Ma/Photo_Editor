#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:00:51 2019

@author: qingchuan-ma
"""

import sys
from PyQt5 import QtWidgets, QtGui
from other_windows import CommonHelper, FramelessWindow
from main_window import myWindow


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
