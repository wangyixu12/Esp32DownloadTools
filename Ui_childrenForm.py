# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/Espressif/esptool_ui/childrenForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 368)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 111, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(470, 10, 41, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(470, 170, 41, 16))
        self.label_4.setObjectName("label_4")
        self.binFileComfirm = QtWidgets.QDialogButtonBox(Form)
        self.binFileComfirm.setGeometry(QtCore.QRect(180, 330, 176, 26))
        self.binFileComfirm.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.binFileComfirm.setObjectName("binFileComfirm")
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(12, 32, 521, 122))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.custBinDir_1 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinDir_1.setObjectName("custBinDir_1")
        self.verticalLayout.addWidget(self.custBinDir_1)
        self.custBinDir_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinDir_2.setMinimumSize(QtCore.QSize(390, 0))
        self.custBinDir_2.setObjectName("custBinDir_2")
        self.verticalLayout.addWidget(self.custBinDir_2)
        self.custBinDir_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinDir_3.setObjectName("custBinDir_3")
        self.verticalLayout.addWidget(self.custBinDir_3)
        self.custBinDir_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinDir_4.setObjectName("custBinDir_4")
        self.verticalLayout.addWidget(self.custBinDir_4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.custBinOptBtn_1 = QtWidgets.QToolButton(self.layoutWidget)
        self.custBinOptBtn_1.setObjectName("custBinOptBtn_1")
        self.verticalLayout_3.addWidget(self.custBinOptBtn_1)
        self.custBinOptBtn_2 = QtWidgets.QToolButton(self.layoutWidget)
        self.custBinOptBtn_2.setObjectName("custBinOptBtn_2")
        self.verticalLayout_3.addWidget(self.custBinOptBtn_2)
        self.custBinOptBtn_3 = QtWidgets.QToolButton(self.layoutWidget)
        self.custBinOptBtn_3.setObjectName("custBinOptBtn_3")
        self.verticalLayout_3.addWidget(self.custBinOptBtn_3)
        self.custBinOptBtn_4 = QtWidgets.QToolButton(self.layoutWidget)
        self.custBinOptBtn_4.setObjectName("custBinOptBtn_4")
        self.verticalLayout_3.addWidget(self.custBinOptBtn_4)
        self.horizontalLayout.addLayout(self.verticalLayout_3)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.custBinOffset_1 = QtWidgets.QLineEdit(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.custBinOffset_1.sizePolicy().hasHeightForWidth())
        self.custBinOffset_1.setSizePolicy(sizePolicy)
        self.custBinOffset_1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.custBinOffset_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.custBinOffset_1.setText("")
        self.custBinOffset_1.setObjectName("custBinOffset_1")
        self.verticalLayout_2.addWidget(self.custBinOffset_1)
        self.custBinOffset_2 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinOffset_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.custBinOffset_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.custBinOffset_2.setObjectName("custBinOffset_2")
        self.verticalLayout_2.addWidget(self.custBinOffset_2)
        self.custBinOffset_3 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinOffset_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.custBinOffset_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.custBinOffset_3.setObjectName("custBinOffset_3")
        self.verticalLayout_2.addWidget(self.custBinOffset_3)
        self.custBinOffset_4 = QtWidgets.QLineEdit(self.layoutWidget)
        self.custBinOffset_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.custBinOffset_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.custBinOffset_4.setObjectName("custBinOffset_4")
        self.verticalLayout_2.addWidget(self.custBinOffset_4)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(11, 190, 521, 124))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.pieBinDir_1 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinDir_1.setObjectName("pieBinDir_1")
        self.verticalLayout_7.addWidget(self.pieBinDir_1)
        self.pieBinDir_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinDir_2.setMinimumSize(QtCore.QSize(390, 0))
        self.pieBinDir_2.setObjectName("pieBinDir_2")
        self.verticalLayout_7.addWidget(self.pieBinDir_2)
        self.pieBinDir_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinDir_3.setObjectName("pieBinDir_3")
        self.verticalLayout_7.addWidget(self.pieBinDir_3)
        self.pieBinDir_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinDir_4.setObjectName("pieBinDir_4")
        self.verticalLayout_7.addWidget(self.pieBinDir_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.pieBinOptBtn_1 = QtWidgets.QToolButton(self.layoutWidget1)
        self.pieBinOptBtn_1.setObjectName("pieBinOptBtn_1")
        self.verticalLayout_8.addWidget(self.pieBinOptBtn_1)
        self.pieBinOptBtn_2 = QtWidgets.QToolButton(self.layoutWidget1)
        self.pieBinOptBtn_2.setObjectName("pieBinOptBtn_2")
        self.verticalLayout_8.addWidget(self.pieBinOptBtn_2)
        self.pieBinOptBtn_3 = QtWidgets.QToolButton(self.layoutWidget1)
        self.pieBinOptBtn_3.setObjectName("pieBinOptBtn_3")
        self.verticalLayout_8.addWidget(self.pieBinOptBtn_3)
        self.pieBinOptBtn_4 = QtWidgets.QToolButton(self.layoutWidget1)
        self.pieBinOptBtn_4.setObjectName("pieBinOptBtn_4")
        self.verticalLayout_8.addWidget(self.pieBinOptBtn_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.pieBinOffset_1 = QtWidgets.QLineEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pieBinOffset_1.sizePolicy().hasHeightForWidth())
        self.pieBinOffset_1.setSizePolicy(sizePolicy)
        self.pieBinOffset_1.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pieBinOffset_1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pieBinOffset_1.setObjectName("pieBinOffset_1")
        self.verticalLayout_9.addWidget(self.pieBinOffset_1)
        self.pieBinOffset_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinOffset_2.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pieBinOffset_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pieBinOffset_2.setObjectName("pieBinOffset_2")
        self.verticalLayout_9.addWidget(self.pieBinOffset_2)
        self.pieBinOffset_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinOffset_3.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pieBinOffset_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pieBinOffset_3.setObjectName("pieBinOffset_3")
        self.verticalLayout_9.addWidget(self.pieBinOffset_3)
        self.pieBinOffset_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.pieBinOffset_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pieBinOffset_4.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pieBinOffset_4.setObjectName("pieBinOffset_4")
        self.verticalLayout_9.addWidget(self.pieBinOffset_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_9)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.custBinDir_1, self.custBinOptBtn_1)
        Form.setTabOrder(self.custBinOptBtn_1, self.custBinOffset_1)
        Form.setTabOrder(self.custBinOffset_1, self.custBinDir_2)
        Form.setTabOrder(self.custBinDir_2, self.custBinOptBtn_2)
        Form.setTabOrder(self.custBinOptBtn_2, self.custBinOffset_2)
        Form.setTabOrder(self.custBinOffset_2, self.custBinDir_3)
        Form.setTabOrder(self.custBinDir_3, self.custBinOptBtn_3)
        Form.setTabOrder(self.custBinOptBtn_3, self.custBinOffset_3)
        Form.setTabOrder(self.custBinOffset_3, self.custBinDir_4)
        Form.setTabOrder(self.custBinDir_4, self.custBinOptBtn_4)
        Form.setTabOrder(self.custBinOptBtn_4, self.custBinOffset_4)
        Form.setTabOrder(self.custBinOffset_4, self.pieBinDir_1)
        Form.setTabOrder(self.pieBinDir_1, self.pieBinOptBtn_1)
        Form.setTabOrder(self.pieBinOptBtn_1, self.pieBinOffset_1)
        Form.setTabOrder(self.pieBinOffset_1, self.pieBinDir_2)
        Form.setTabOrder(self.pieBinDir_2, self.pieBinOptBtn_2)
        Form.setTabOrder(self.pieBinOptBtn_2, self.pieBinOffset_2)
        Form.setTabOrder(self.pieBinOffset_2, self.pieBinDir_3)
        Form.setTabOrder(self.pieBinDir_3, self.pieBinOptBtn_3)
        Form.setTabOrder(self.pieBinOptBtn_3, self.pieBinOffset_3)
        Form.setTabOrder(self.pieBinOffset_3, self.pieBinDir_4)
        Form.setTabOrder(self.pieBinDir_4, self.pieBinOptBtn_4)
        Form.setTabOrder(self.pieBinOptBtn_4, self.pieBinOffset_4)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Origin Bin Firmware Setting"))
        self.label_2.setText(_translate("Form", "Pie file dir"))
        self.label.setText(_translate("Form", "Customer file dir"))
        self.label_3.setText(_translate("Form", "offset"))
        self.label_4.setText(_translate("Form", "offset"))
        self.custBinOptBtn_1.setText(_translate("Form", "..."))
        self.custBinOptBtn_2.setText(_translate("Form", "..."))
        self.custBinOptBtn_3.setText(_translate("Form", "..."))
        self.custBinOptBtn_4.setText(_translate("Form", "..."))
        self.pieBinOptBtn_1.setText(_translate("Form", "..."))
        self.pieBinOptBtn_2.setText(_translate("Form", "..."))
        self.pieBinOptBtn_3.setText(_translate("Form", "..."))
        self.pieBinOptBtn_4.setText(_translate("Form", "..."))

