'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-09 09:46:35
@Description: 调用ui函数
'''
import os
import sys
import yaml
import codecs
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from editYaml import optYaml
from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        # self.yaml = optYaml()
        self._defaultYamlName = 'configDefault.yml'
        self._userYamlName = 'configUser.yml'
        self.loadYaml()
        
        
    
        layout = QVBoxLayout()
        
        self.setupUi(self)
        self.child = ChildrenForm()
        self.actOriFw.triggered.connect(self.childShow)
        self.custFwOptBtn.clicked.connect(self.openDir)
        self.pieFwOptBtn.clicked.connect(self.openDir)

    def loadYaml(self):
        if os._exists(self._userYamlName) == False:
            self.configFile = codecs.open(self._defaultYamlName, 'r', encoding='utf-8')
        else:
            self.configFile = codecs.open(self._userYamlName, 'w+', encoding='utf-8')
        self.config = yaml.load(self.configFile, yaml.Loader)                
        print(self.config)

    # def setWin(self):
        

    def openDir(self):
        btn_dict = {self.custFwOptBtn: self.custFwEdit, self.pieFwOptBtn: self.pieFwEdit}
        assert(self.sender() in btn_dict.keys())
        file, ok= QFileDialog.getOpenFileName(self, "Open", "~/", "Binary Files(*.bin)")
        btn_dict[self.sender()].setText(file)
        
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
    