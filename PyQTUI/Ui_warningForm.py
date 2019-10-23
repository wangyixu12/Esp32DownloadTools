# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wyx/Documents/pi/DC5270/Esp32DownloadTools/PyQTUI/warningForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warning_obj(object):
    def setupUi(self, Warning_obj):
        Warning_obj.setObjectName("Warning_obj")
        Warning_obj.resize(650, 263)
        Warning_obj.setMinimumSize(QtCore.QSize(587, 198))
        Warning_obj.setMaximumSize(QtCore.QSize(650, 300))
        self.warn_png = QtWidgets.QLabel(Warning_obj)
        self.warn_png.setGeometry(QtCore.QRect(20, 30, 71, 71))
        self.warn_png.setText("")
        self.warn_png.setPixmap(QtGui.QPixmap("img/waring.png"))
        self.warn_png.setObjectName("warn_png")
        self.confirm_btn = QtWidgets.QPushButton(Warning_obj)
        self.confirm_btn.setGeometry(QtCore.QRect(230, 210, 98, 26))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.confirm_btn.setFont(font)
        self.confirm_btn.setObjectName("confirm_btn")
        self.label_2 = QtWidgets.QLabel(Warning_obj)
        self.label_2.setGeometry(QtCore.QRect(120, 20, 531, 181))
        self.label_2.setMinimumSize(QtCore.QSize(461, 121))
        self.label_2.setMaximumSize(QtCore.QSize(600, 200))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Warning_obj)
        QtCore.QMetaObject.connectSlotsByName(Warning_obj)

    def retranslateUi(self, Warning_obj):
        _translate = QtCore.QCoreApplication.translate
        Warning_obj.setWindowTitle(_translate("Warning_obj", "Warning"))
        self.confirm_btn.setText(_translate("Warning_obj", "I KNOW"))
        self.label_2.setText(_translate("Warning_obj", "<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; font-style:italic; color:#ff0000;\">WARNING: </span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ca2d2d;\">Flashing of customer firmware is allowed only once.</span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ca2d2d;\">The customer firmware is encrypted any further </span></p><p><span style=\" font-size:14pt; font-weight:600; color:#ca2d2d;\">flashing operation will corrupt the units system!</span></p></body></html>"))
