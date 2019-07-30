# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.setEnabled(True)
        Dialog.resize(487, 378)
        Dialog.setMaximumSize(QtCore.QSize(487, 400))
        Dialog.setFocusPolicy(QtCore.Qt.NoFocus)
        Dialog.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.gridLayout_2 = QtWidgets.QGridLayout(Dialog)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setVerticalSpacing(1)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setEnabled(True)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 148, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout.addWidget(self.line, 2, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 58, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 0, 1, 1)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.plainTextEdit.setStyleSheet("background: transparent;    ")
        self.plainTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setBackgroundVisible(False)
        self.plainTextEdit.setCenterOnScroll(False)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 1, 2, 1)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setEnabled(True)
        self.plainTextEdit_2.setStyleSheet("background: transparent;    ")
        self.plainTextEdit_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.plainTextEdit_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.gridLayout.addWidget(self.plainTextEdit_2, 3, 1, 2, 1)
        self.gridLayout.setRowStretch(4, 4)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "About Photo Editor"))
        self.label.setText(_translate("Dialog", "操作手册"))
        self.label_2.setText(_translate("Dialog", "制作团队"))
        self.plainTextEdit.setPlainText(_translate("Dialog", "1. 可以调整打开图片的五官，包括眼睛，鼻子，嘴唇，眼睛和脸颊\n"
"2. 可以在祛痘模式通过双击图片区域在部分区域内进行祛痘\n"
"3.五官可反复调整，但祛痘模式下将自动保存你所做的调整，即在之后调整五官会在保存的基础上继续调整\n"
"4.可以更换图片背景，添加贴图，更换11种滤镜，甚至换脸"))
        self.plainTextEdit_2.setPlainText(_translate("Dialog", "马清川  1600011621                   王雯琦  1700012879\n"
"王    瞬  1600011621                   邢博威  1700012879\n"
"吕天烨  1600011621                   张佳琪  1700012879\n"
"隋    垚  1600011621                   王晨茜  1700012879\n"
"\n"
"仅作为课程作业，严禁商用"))
