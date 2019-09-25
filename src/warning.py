'''
@Author: Yixu Wang
@Github: https://github.com/wangyixu12
@Date: 2019-09-25 11:20:06
@LastEditors: Yixu Wang
@LastEditTime: 2019-09-25 11:33:31
@Description: Warning Form
'''

import sys
sys.path.append("..")


from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt

from PyQTUI.Ui_warningForm import Ui_Warning_obj

class WarnTip(QWidget, Ui_Warning_obj):
    def __init__(self):
        super(WarnTip, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = WarnTip()
    win.show()
    app.exec_()