#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 17:00:51 2019

@author: qingchuan-ma
"""

import sys
from PyQt5 import QtWidgets
import main_window

if __name__ == '__main__':
    if not QtWidgets.QApplication.instance():
        app = QtWidgets.QApplication(sys.argv)
    else:
        app = QtWidgets.QApplication.instance()
    app.aboutToQuit.connect(app.deleteLater)
    mywindow = main_window.myWindow()
    mywindow.show()
    app.exec_()