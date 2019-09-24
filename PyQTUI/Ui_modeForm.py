# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/Espressif/esptool_ui/PyQTUI/modeForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mode_obj(object):
    def setupUi(self, mode_obj):
        mode_obj.setObjectName("mode_obj")
        mode_obj.resize(191, 163)
        mode_obj.setAcceptDrops(False)
        self.tester_mode_btn = QtWidgets.QPushButton(mode_obj)
        self.tester_mode_btn.setGeometry(QtCore.QRect(40, 20, 121, 51))
        self.tester_mode_btn.setObjectName("tester_mode_btn")
        self.cust_mode_btn = QtWidgets.QPushButton(mode_obj)
        self.cust_mode_btn.setGeometry(QtCore.QRect(40, 90, 121, 51))
        self.cust_mode_btn.setObjectName("cust_mode_btn")

        self.retranslateUi(mode_obj)
        QtCore.QMetaObject.connectSlotsByName(mode_obj)

    def retranslateUi(self, mode_obj):
        _translate = QtCore.QCoreApplication.translate
        mode_obj.setWindowTitle(_translate("mode_obj", "Select Mode"))
        self.tester_mode_btn.setText(_translate("mode_obj", "Tester "))
        self.cust_mode_btn.setText(_translate("mode_obj", "Customer"))

