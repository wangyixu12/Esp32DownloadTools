'''
@Author: Yixu Wang
@Github: https://github.com/wangyixu12
@Date: 2019-09-24 16:19:29
@LastEditors: Yixu Wang
@LastEditTime: 2019-09-24 16:37:52
@Description: Select download mode (1. Tester 2. Customer) 
'''

import sys

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQTUI.Ui_modeForm import Ui_mode_obj

class SelectMode(QWidget, Ui_mode_obj):
    def __init__(self):
        super(SelectMode, self).__init__()
        self.mode = None
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.tester_mode_btn.clicked.connect(self.__select_tester)
        self.cust_mode_btn.clicked.connect(self.__select_custer)

    def __select_tester(self):
        self.mode = 'tester'
        self.close()

    def __select_custer(self):
        self.mode = 'custer'
        self.close()