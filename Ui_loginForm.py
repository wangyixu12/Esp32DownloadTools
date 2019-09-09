# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/wyx/Documents/Esp32DownloadTools/loginForm.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_loginForm(object):
    def setupUi(self, loginForm):
        loginForm.setObjectName("loginForm")
        loginForm.resize(243, 115)
        loginForm.setMinimumSize(QtCore.QSize(243, 115))
        loginForm.setMaximumSize(QtCore.QSize(243, 115))
        self.layoutWidget = QtWidgets.QWidget(loginForm)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 221, 60))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.user_name_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.user_name_edit.setObjectName("user_name_edit")
        self.verticalLayout.addWidget(self.user_name_edit)
        self.password_edit = QtWidgets.QLineEdit(self.layoutWidget)
        self.password_edit.setObjectName("password_edit")
        self.verticalLayout.addWidget(self.password_edit)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(loginForm)
        self.layoutWidget1.setGeometry(QtCore.QRect(30, 80, 189, 27))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.login_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.login_btn.setObjectName("login_btn")
        self.horizontalLayout_2.addWidget(self.login_btn)
        self.cancle_btn = QtWidgets.QPushButton(self.layoutWidget1)
        self.cancle_btn.setObjectName("cancle_btn")
        self.horizontalLayout_2.addWidget(self.cancle_btn)

        self.retranslateUi(loginForm)
        QtCore.QMetaObject.connectSlotsByName(loginForm)

    def retranslateUi(self, loginForm):
        _translate = QtCore.QCoreApplication.translate
        loginForm.setWindowTitle(_translate("loginForm", "Form"))
        self.label.setText(_translate("loginForm", "USER"))
        self.label_2.setText(_translate("loginForm", "PASSWORD"))
        self.login_btn.setText(_translate("loginForm", "Login"))
        self.cancle_btn.setText(_translate("loginForm", "Cancel"))
