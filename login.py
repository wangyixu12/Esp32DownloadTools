'''
@Description: In User Settings Edit
@Author: your name
@Date: 2019-09-08 11:24:28
@LastEditTime: 2019-09-21 09:38:33
@LastEditors: Yixu Wang
'''
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import Qt

from PyQTUI.Ui_loginForm import Ui_loginForm

class LoginForm(QWidget, Ui_loginForm):
    ResultSignal = pyqtSignal(str)
    user_name = "admin"
    user_password = "pi1234"
    def __init__(self):
        super(LoginForm, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self.password_edit.setEchoMode(QLineEdit.Password)
        self.login_btn.clicked.connect(self.__login)
        self.cancle_btn.clicked.connect(self.__cancle)

    def __login(self):
        user_name = self.user_name_edit.text()
        password = self.password_edit.text()
        if (user_name == self.user_name) and (password == self.user_password):
            self.user_name_edit.clear()
            self.password_edit.clear()
            self.close()
            self.ResultSignal.emit('login')
        else:
            self.user_name_edit.setText("ERROR")
            self.password_edit.clear()
            # self.password_edit.setText("ERROR")
            # self.ResultSignal.emit('close')

    def __cancle(self):
        self.user_name_edit.clear()
        self.password_edit.clear()
        self.close()
        self.ResultSignal.emit('close')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LoginForm()
    win.show()
    app.exec_()
    