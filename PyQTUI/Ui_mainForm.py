# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/pi/Documents/Espressif/esptool_ui/PyQTUI/mainForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(532, 467)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(532, 467))
        MainWindow.setMaximumSize(QtCore.QSize(532, 467))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 531, 311))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setMinimumSize(QtCore.QSize(0, 20))
        self.label_4.setMaximumSize(QtCore.QSize(60, 25))
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.resultTextBrowser = QtWidgets.QTextBrowser(self.layoutWidget)
        self.resultTextBrowser.setMaximumSize(QtCore.QSize(530, 400))
        self.resultTextBrowser.setObjectName("resultTextBrowser")
        self.verticalLayout.addWidget(self.resultTextBrowser)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 370, 251, 30))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.portComBox = QtWidgets.QComboBox(self.layoutWidget1)
        self.portComBox.setMinimumSize(QtCore.QSize(50, 26))
        self.portComBox.setMaximumSize(QtCore.QSize(300, 26))
        self.portComBox.setObjectName("portComBox")
        self.horizontalLayout_3.addWidget(self.portComBox)
        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)
        self.searchPortBtn = QtWidgets.QPushButton(self.layoutWidget1)
        self.searchPortBtn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.searchPortBtn.setObjectName("searchPortBtn")
        self.horizontalLayout_5.addWidget(self.searchPortBtn)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 310, 250, 53))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pieFlashBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.pieFlashBtn.setMinimumSize(QtCore.QSize(121, 51))
        self.pieFlashBtn.setMaximumSize(QtCore.QSize(121, 51))
        self.pieFlashBtn.setObjectName("pieFlashBtn")
        self.horizontalLayout_2.addWidget(self.pieFlashBtn)
        self.custFlashBtn = QtWidgets.QPushButton(self.layoutWidget2)
        self.custFlashBtn.setMinimumSize(QtCore.QSize(121, 51))
        self.custFlashBtn.setMaximumSize(QtCore.QSize(121, 51))
        self.custFlashBtn.setObjectName("custFlashBtn")
        self.horizontalLayout_2.addWidget(self.custFlashBtn)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(290, 320, 221, 121))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.layoutWidget_2)
        self.label_5.setMinimumSize(QtCore.QSize(0, 20))
        self.label_5.setMaximumSize(QtCore.QSize(60, 25))
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.resultBrowser = QtWidgets.QTextBrowser(self.layoutWidget_2)
        self.resultBrowser.setMaximumSize(QtCore.QSize(250, 100))
        self.resultBrowser.setObjectName("resultBrowser")
        self.verticalLayout_2.addWidget(self.resultBrowser)
        self.layoutWidget3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 410, 181, 27))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget3)
        self.label.setMaximumSize(QtCore.QSize(72, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.baudComboBox = QtWidgets.QComboBox(self.layoutWidget3)
        self.baudComboBox.setDuplicatesEnabled(False)
        self.baudComboBox.setObjectName("baudComboBox")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.baudComboBox.addItem("")
        self.horizontalLayout.addWidget(self.baudComboBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 532, 23))
        self.menubar.setObjectName("menubar")
        self.menuSetting = QtWidgets.QMenu(self.menubar)
        self.menuSetting.setObjectName("menuSetting")
        MainWindow.setMenuBar(self.menubar)
        self.setPieFwDir = QtWidgets.QAction(MainWindow)
        self.setPieFwDir.setObjectName("setPieFwDir")
        self.setCoutFwDir = QtWidgets.QAction(MainWindow)
        self.setCoutFwDir.setObjectName("setCoutFwDir")
        self.actVeriFw = QtWidgets.QAction(MainWindow)
        self.actVeriFw.setObjectName("actVeriFw")
        self.actFlashFw = QtWidgets.QAction(MainWindow)
        self.actFlashFw.setObjectName("actFlashFw")
        self.act_login = QtWidgets.QAction(MainWindow)
        self.act_login.setObjectName("act_login")
        self.menuSetting.addAction(self.actVeriFw)
        self.menuSetting.addAction(self.actFlashFw)
        self.menuSetting.addAction(self.act_login)
        self.menubar.addAction(self.menuSetting.menuAction())
        self.label_4.setBuddy(self.resultTextBrowser)
        self.label_3.setBuddy(self.portComBox)
        self.label_5.setBuddy(self.resultTextBrowser)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Esp32 Download Tools"))
        self.label_4.setText(_translate("MainWindow", "Flow"))
        self.label_3.setText(_translate("MainWindow", "&PORT"))
        self.searchPortBtn.setText(_translate("MainWindow", "Search"))
        self.pieFlashBtn.setText(_translate("MainWindow", "Flash\n"
"Tester FW"))
        self.custFlashBtn.setText(_translate("MainWindow", "Flash\n"
"Customer FW"))
        self.label_5.setText(_translate("MainWindow", "Result"))
        self.label.setText(_translate("MainWindow", "Baud Rate"))
        self.baudComboBox.setCurrentText(_translate("MainWindow", "2000000"))
        self.baudComboBox.setItemText(0, _translate("MainWindow", "2000000"))
        self.baudComboBox.setItemText(1, _translate("MainWindow", "1152000"))
        self.baudComboBox.setItemText(2, _translate("MainWindow", "921600"))
        self.baudComboBox.setItemText(3, _translate("MainWindow", "230400"))
        self.baudComboBox.setItemText(4, _translate("MainWindow", "115200"))
        self.baudComboBox.setItemText(5, _translate("MainWindow", "96000"))
        self.menuSetting.setTitle(_translate("MainWindow", "Configure"))
        self.setPieFwDir.setText(_translate("MainWindow", "Pie"))
        self.setPieFwDir.setShortcut(_translate("MainWindow", "Ctrl+S, Ctrl+P"))
        self.setCoutFwDir.setText(_translate("MainWindow", "Customer"))
        self.actVeriFw.setText(_translate("MainWindow", "Verify Firmware"))
        self.actFlashFw.setText(_translate("MainWindow", "Flash Firmware"))
        self.act_login.setText(_translate("MainWindow", "Login"))

