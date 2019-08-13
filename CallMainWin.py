'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-13 10:07:32
@Description: 调用ui函数
'''
import os
import sys
import yaml
import codecs
import shutil
import time
import threading

from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

# from esptool import esptool
import esptool

# from editYaml import optYaml
from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form


class MyMainWindow(QMainWindow, Ui_MainWindow):
    
    ERASE_PASS = "Erase flash ------> PASS\n"
    ERASE_FAIL = "Erase flash ------> FAIL\n"
    WRITE_PASS = "Write flash ------> PASS\n"
    WRITE_FAIL = "Write flash ------> FAIL\n"
        
    BAUD = 1152000

    TEST_FLASH = 'test'
    CUST_FLASH = 'customer'

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
        
        self.port=''

        self.child = ChildrenForm()
        self.pieFwEdit.setReadOnly(True)
        self.custFwEdit.setReadOnly(True)
        self.resultTextEdit.setReadOnly(True)
        self.actOriFw.triggered.connect(self.childShow)
        self.custFwOptBtn.clicked.connect(self.openDir)
        self.pieFwOptBtn.clicked.connect(self.openDir)
        self.custFlashBtn.clicked.connect(self.custFlash)
        self.searchPortBtn.clicked.connect(self.searchVarPort)
        self.portComBox.currentIndexChanged.connect(self.selectComPort)

    def checkSetting(self, choose):
        assert((choose == self.CUST_FLASH) | (choose == self.TEST_FLASH))
        ret = True
        try:
            assert(self.port != '')
        except:
            self.resultTextEdit.setPlainText(self.ERASE_FAIL+"E: Port not set\n")
            ret = False

        if choose == 'test':
            try:
                assert(self.pieFwEdit.text() != '')
            except:
                self.resultTextEdit.append(self.WRITE_FAIL+'E: Test Fw not set\n')
                ret = ret & False
        elif choose == self.CUST_FLASH:
            try:
                assert(self.custFwEdit.text() != '')
            except:
                self.resultTextEdit.append(self.WRITE_FAIL+'E: Customer Fw not set\n')
                ret = ret & False
        return ret

    def eraseFlash(self):
        command = ['--port', str(self.port), 'erase_flash']
        esptool.main(command)
        self.resultTextEdit.setPlainText(self.ERASE_PASS)
        self.flashProcessBar.setValue(10)

    def writeFlash(self, binFilePath):
        command = ['--chip', 'esp32', '--port', str(self.port), '--baud', str(self.BAUD),\
            '--before', 'default_reset', '--after', 'hard_reset', 'write_flash', '0x0000', binFilePath]
        esptool.main(command)
        self.resultTextEdit.append(self.ERASE_PASS)
        self.flashProcessBar.setValue(40)

    def varifyFlash(self):
        pass
        


    def custFlash(self):
        self.flashProcessBar.setValue(0)
        self.resultTextEdit.clear()
        if self.checkSetting(self.CUST_FLASH) == False:
            return
        self.eraseFlash()
        self.writeFlash(self.custFwEdit.text())

    def searchVarPort(self):
        varifyPort = QSerialPortInfo.availablePorts()
        if varifyPort == None:
            return
        self.portComBox.clear()
        for serPortInfo in varifyPort:
            if 'USB' not in serPortInfo.portName():
                continue
            self.portComBox.addItem(serPortInfo.portName())

    def selectComPort(self):
        curPort = QSerialPortInfo(self.portComBox.currentText())
        self.curPortLocation = curPort.systemLocation()
        self.port = self.curPortLocation

    def loadYaml(self):
        if os.path.exists(self._userYamlName) == False:
            shutil.copyfile(self._defaultYamlName, self._userYamlName)
        self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        self.config = yaml.load(self.configFile, yaml.Loader)

        defConfigFile = codecs.open(self._defaultYamlName, 'r', encoding='utf-8')           
        defConfig = yaml.load(defConfigFile, yaml.Loader)

        for winName, secondDict in defConfig.items():
            for editLine in secondDict.keys():
                if editLine not in self.config[winName].keys():
                    shutil.copyfile(self._defaultYamlName, self._userYamlName)
                    self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
                    self.config = yaml.load(self.configFile, yaml.Loader)
                    return 

    def editYaml(self, winName, key, value):
        # self.config = yaml.load(self.configFile, yaml.Loader)
        configFileEdit = codecs.open(self._userYamlName, 'w', encoding='utf-8')
        data = self.config
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
        self.child.run()

    def run(self):
        self.loadYaml()
        self.setWin()

class ChildrenForm(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)
        self._defaultYamlName = 'configDefault.yml'
        self._userYamlName = 'configUser.yml'

        self._winName = 'childrenForm'
        self._winEditDict = {
            self.custBinDir_1: "custBinDir_1",
            self.custBinDir_2: "custBinDir_2",
            self.custBinDir_3: "custBinDir_3",
            self.custBinDir_4: "custBinDir_4",

            self.custBinOffset_1: "custBinOffset_1",
            self.custBinOffset_2: "custBinOffset_2",
            self.custBinOffset_3: "custBinOffset_3",
            self.custBinOffset_4: "custBinOffset_4",

            self.pieBinDir_1: "pieBinDir_1",
            self.pieBinDir_2: "pieBinDir_2",
            self.pieBinDir_3: "pieBinDir_3",
            self.pieBinDir_4: "pieBinDir_4",

            self.pieBinOffset_1: "pieBinOffset_1",
            self.pieBinOffset_2: "pieBinOffset_2",
            self.pieBinOffset_3: "pieBinOffset_3",
            self.pieBinOffset_4: "pieBinOffset_4",
        }
        
        self.custBinOptBtn_1.clicked.connect(self.openDir)
        self.custBinOptBtn_2.clicked.connect(self.openDir)
        self.custBinOptBtn_3.clicked.connect(self.openDir)
        self.custBinOptBtn_4.clicked.connect(self.openDir)

        self.pieBinOptBtn_1.clicked.connect(self.openDir)
        self.pieBinOptBtn_2.clicked.connect(self.openDir)
        self.pieBinOptBtn_3.clicked.connect(self.openDir)
        self.pieBinOptBtn_4.clicked.connect(self.openDir)
        
        self.binFileComfirm.button(self.binFileComfirm.Save).clicked.connect(self._save)
        self.binFileComfirm.button(self.binFileComfirm.Discard).clicked.connect(self._discard)        

    def _save(self):
        for editKey in self._winEditDict.keys():
            text = editKey.text()
            self.editYaml(self._winName, self._winEditDict[editKey], text)
        self.close()

    def _discard(self):
        self.close()

    def editYaml(self, winName, key, value):
        # self.config = yaml.load(self.configFile, yaml.Loader)
        configFileEdit = codecs.open(self._userYamlName, 'w', encoding='utf-8')
        data = self.config
        data[winName][key] = value
        data.update()
        yaml.dump(data, configFileEdit, yaml.SafeDumper)
        configFileEdit.close()

    def openDir(self):
        btn_dict = {
            self.custBinOptBtn_1: self.custBinDir_1,
            self.custBinOptBtn_2: self.custBinDir_2,
            self.custBinOptBtn_3: self.custBinDir_3,
            self.custBinOptBtn_4: self.custBinDir_4,

            self.pieBinOptBtn_1: self.pieBinDir_1,
            self.pieBinOptBtn_2: self.pieBinDir_2,
            self.pieBinOptBtn_3: self.pieBinDir_3,
            self.pieBinOptBtn_4: self.pieBinDir_4,
        }
        assert(self.sender() in btn_dict.keys())
        file, ok = QFileDialog.getOpenFileName(self, "Open", './', 'Binary Files(*.bin)')
        btn_dict[self.sender()].setText(file)
        # self.editYaml(self._winName, self._winEditDict[btn_dict[self.sender()]], file)
        
    def setWin(self):
        for key, file in self._winEditDict.items():
            key.setText(self.config[self._winName][file])

    def loadYaml(self):
        if os.path.exists(self._userYamlName) == False:
            shutil.copyfile(self._defaultYamlName, self._userYamlName)
        self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        self.config = yaml.load(self.configFile, yaml.Loader)

    def run(self):
        self.loadYaml()
        self.setWin()

def main():
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.run()
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    