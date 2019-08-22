# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/Espressif/esptool_ui/flashSetForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_flashSetForm(object):
    def setupUi(self, flashSetForm):
        flashSetForm.setObjectName("flashSetForm")
        flashSetForm.resize(291, 167)
        self.layoutWidget = QtWidgets.QWidget(flashSetForm)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 10, 251, 104))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pieFwEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.pieFwEdit.setObjectName("pieFwEdit")
        self.horizontalLayout.addWidget(self.pieFwEdit)
        self.pieFwOptBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.pieFwOptBtn.setObjectName("pieFwOptBtn")
        self.horizontalLayout.addWidget(self.pieFwOptBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.custFwEdit = QtWidgets.QLineEdit(self.layoutWidget)
        self.custFwEdit.setObjectName("custFwEdit")
        self.horizontalLayout_4.addWidget(self.custFwEdit)
        self.custFwOptBtn = QtWidgets.QToolButton(self.layoutWidget)
        self.custFwOptBtn.setObjectName("custFwOptBtn")
        self.horizontalLayout_4.addWidget(self.custFwOptBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.binFileComfirm = QtWidgets.QDialogButtonBox(flashSetForm)
        self.binFileComfirm.setGeometry(QtCore.QRect(20, 130, 251, 26))
        self.binFileComfirm.setStandardButtons(QtWidgets.QDialogButtonBox.Discard|QtWidgets.QDialogButtonBox.Save)
        self.binFileComfirm.setCenterButtons(True)
        self.binFileComfirm.setObjectName("binFileComfirm")

        self.retranslateUi(flashSetForm)
        QtCore.QMetaObject.connectSlotsByName(flashSetForm)

    def retranslateUi(self, flashSetForm):
        _translate = QtCore.QCoreApplication.translate
        flashSetForm.setWindowTitle(_translate("flashSetForm", "Flash Setting"))
        self.label_2.setText(_translate("flashSetForm", "Test Firmware"))
        self.pieFwOptBtn.setText(_translate("flashSetForm", "..."))
        self.label.setText(_translate("flashSetForm", "Customer Firmware"))
        self.custFwOptBtn.setText(_translate("flashSetForm", "..."))

