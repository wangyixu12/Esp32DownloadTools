'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-09 13:24:21
@Description: 调用ui函数
'''
import os
import sys
import yaml
import codecs
import shutil
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from editYaml import optYaml
from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.yaml = optYaml()
        self._defaultYamlName = 'configDefault.yml'
        self._userYamlName = 'configUser.yml'

        self._winName = 'mainForm'
        self._winEditDict = {
            self.custFwEdit: 'custFwEdit',
            self.pieFwEdit: 'pieFwEdit',
        }
        self.loadYaml()
        self.setWin()
        
    
        layout = QVBoxLayout()
        
        # self.setupUi(self)
        self.child = ChildrenForm()
        self.actOriFw.triggered.connect(self.childShow)
        self.custFwOptBtn.clicked.connect(self.openDir)
        self.pieFwOptBtn.clicked.connect(self.openDir)

    def loadYaml(self):
        if os.path.exists(self._userYamlName) == False:
            shutil.copyfile(self._defaultYamlName, self._userYamlName)
        self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        self.config = yaml.load(self.configFile, yaml.Loader)         

    def editYaml(self, winName, key, value):
        configFileEdit = codecs.open(self._userYamlName, 'w', encoding='utf-8')
        data = self.config
        print(data)
        data[winName][key] = value
        data.update()
        yaml.dump(data, configFileEdit, yaml.SafeDumper)
        configFileEdit.close()

    def setWin(self):
        for key, file in self._winEditDict.items():
            key.setText(self.config[self._winName][file])

    def openDir(self):
        btn_dict = {self.custFwOptBtn: self.custFwEdit, self.pieFwOptBtn: self.pieFwEdit}
        assert(self.sender() in btn_dict.keys())
        file, ok= QFileDialog.getOpenFileName(self, "Open", "./", "Binary Files(*.bin)")
        btn_dict[self.sender()].setText(file)
        self.editYaml(self._winName, self._winEditDict[btn_dict[self.sender()]], file)
        
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
    