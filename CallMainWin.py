'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-08 14:26:00
@Description: 调用ui函数
'''
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QWidget
from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.child = ChildrenForm()
        # self.setPieFwDir.triggered.connect(self.openMsg)
        self.actOriFw.triggered.connect(self.childShow)
        
    def openMsg(self,):
        file, ok = QFileDialog.getOpenFileName(self, "Open", "~/", "All Files (*);;Text Files (*.txt)")
        self.statusBar.showMessage(file)
    
    def childShow(self):
        # self.MaingridLayout.addWidget(self.child)
        self.child.show()

class ChildrenForm(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())
    