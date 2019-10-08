'''
@Author: Yixu Wang
@Github: https://github.com/wangyixu12
@Date: 2019-09-25 11:20:06
@LastEditors: Yixu Wang
@LastEditTime: 2019-10-08 09:03:18
@Description: Warning Form
'''

import sys
sys.path.append("../")
from time import sleep

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QTimer

from PyQTUI.Ui_warningForm import Ui_Warning_obj

class WarnTip(QWidget, Ui_Warning_obj):
    def __init__(self):
        super(WarnTip, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMaximizeButtonHint)
        self._time = QTimer()
        self.confirm_btn.setEnabled(False)
        self.confirm_btn.clicked.connect(self.close)

    def countdown(self,):
        time = 10
        for idx in range(time):
            self.confirm_btn.setText("wait "+str(time-idx)+'s')
            QApplication.processEvents()
            sleep(1)
        else:
            self.confirm_btn.setEnabled(True)
            self.confirm_btn.setText("I KNOW")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WarnTip()
    win.show()
    win.countdown()
    app.exec_()