'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-22 15:48:28
@Description: 调用ui函数
'''
import os
import sys
import yaml
import codecs
import shutil
import time
import threading

from enum import Enum

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


import esptool

from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form
from Ui_flashSetForm import Ui_flashSetForm

class states(Enum):
    CHECK = 0
    ERASE = 1
    WRITE = 2
    VERIFY = 3
    RESULT = 4

class MyMainWindow(QMainWindow, Ui_MainWindow):
    
    ERASE_PASS = "Erase flash ------> PASS\n"
    ERASE_FAIL = "Erase flash ------> FAIL\n"
    WRITE_PASS = "Write flash ------> PASS\n"
    WRITE_FAIL = "Write flash ------> FAIL\n"
    VARI_PASS = "Verify flash ------> PASS\n"
    VARI_FAIL = "Verify flash ------> FAIL\n"
        
    BAUD = 1152000

    TEST_FLASH = 'test'
    CUST_FLASH = 'customer'

    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self._defaultYamlName = 'configDefault.yml'
        self._userYamlName = 'configUser.yml'

        self.OriBinDict = {
            self.TEST_FLASH : {
                'pieBinDir_1': 'pieBinOffset_1',
                'pieBinDir_2': 'pieBinOffset_2',
                'pieBinDir_3': 'pieBinOffset_3',
                'pieBinDir_4': 'pieBinOffset_4',
            },
            self.CUST_FLASH : {
                'custBinDir_1': 'custBinOffset_1',
                'custBinDir_2': 'custBinOffset_2',
                'custBinDir_3': 'custBinOffset_3',
                'custBinDir_4': 'custBinOffset_4',
            }
        }

        self._transitions = {
            states.CHECK.value : self.checkConf,
            states.ERASE.value : self.eraseFlash,
            states.WRITE.value : self.writeFlash,
            states.VERIFY.value : self.verifyFlash,
            states.RESULT.value : self._dispResult
        }
        
        self.port=''
        self.processTimes = 0
        sys.stdout = EmittingStream(textWritten = self.outputWritten)

        self.child = ChildrenForm()
        self.child.CloseSignal.connect(self._enableBtn)

        self.flashSet = FwSetForm()
        
        self.thread = flashWorkerThread()
        self.thread.finish.connect(self.flash_thread)

        self.resultTextBrowser.setReadOnly(True)
        self.resultBrowser.setReadOnly(True)
        
        self.actVeriFw.triggered.connect(self.childShow)
        self.actFlashFw.triggered.connect(self.flashSetShow)
        self.searchPortBtn.clicked.connect(self.searchVarPort)
        self.portComBox.currentIndexChanged.connect(self.selectComPort)

    def __del__(self):
        sys.stdout = sys.__stdout__
    
    def _enableBtn(self):
        self.pieFlashBtn.setEnabled(True)
        self.custFlashBtn.setEnabled(True)
        self.searchPortBtn.setEnabled(True)
        self.actVeriFw.setEnabled(True)
        self.actFlashFw.setEnabled(True)

    def _disableBtn(self):
        self.pieFlashBtn.setEnabled(False)
        self.custFlashBtn.setEnabled(False)
        self.searchPortBtn.setEnabled(False)
        self.actVeriFw.setEnabled(False)
        self.actFlashFw.setEnabled(False)

    def outputWritten(self, text):
        cursor = self.resultTextBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.resultTextBrowser.setTextCursor(cursor)
        self.resultTextBrowser.ensureCursorVisible()
        

    def _dispResult(self, result):
        # if result == 'FAIL':
        self.resultBrowser.setHtml("<img src='./"+result+".png'>")

    def flash_thread(self, opt, data = None):
        # print(opt, data)
        if data == 'FAIL':
            # 显示fail
            self.resultTextBrowser.append(opt.name + ' --> FAIL')
            self._transitions[states.RESULT.value]("FAIL")
            return
        elif data == 'PASS':
            # 显示PASS
            self.resultTextBrowser.append(opt.name + ' --> PASS')
        if opt == states.VERIFY:
            self._transitions[opt.value + 1](data)
        else: 
            self._transitions[opt.value + 1]()

    def checkConf(self):
        choose = self.optChoose
        assert((choose == self.CUST_FLASH) | (choose == self.TEST_FLASH))
        ret = True
        child = self.child
        configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        yamlConfig = yaml.load(configFile, yaml.Loader)
        configFile.close()

        try:
            assert(self.port != '')
        except:
            self.resultTextBrowser.setPlainText(self.ERASE_FAIL+"E: Port not set\n")
            ret = False

        if choose == self.TEST_FLASH:
            try:
                assert(self.pieFwEdit.text() != '')
            except:
                self.resultTextBrowser.append(self.WRITE_FAIL+'E: Test Fw not set\n')
                ret = ret & False

        elif choose == self.CUST_FLASH:
            try:
                assert(self.custFwEdit.text() != '')
            except:
                self.resultTextBrowser.append(self.WRITE_FAIL+'E: Customer Fw not set\n')
                ret = ret & False

        isContent = False
        for binDir, offset in self.OriBinDict[choose].items():
            isContent = isContent | bool(yamlConfig[self.child._winName][binDir])
            try:
                assert(bool(yamlConfig[self.child._winName][binDir])==bool(yamlConfig[self.child._winName][offset]))
            except:
                self.resultTextBrowser.append(self.VARI_FAIL+
                'E: Origin bin file setting is error:\nPlease check '+ binDir)
                ret = ret & False
                break
        else:
            try:
                assert(isContent)
            except:
                self.resultTextBrowser.append(self.VARI_FAIL+'E: Origin bin file setting is error\n')
                ret = ret & False

        if ret == False:
            self.flash_thread(states.RESULT, 'FAIL')
        else:
            self.flash_thread(states.ERASE)
        
    def eraseFlash(self):
        command = ['--port', str(self.port), 'erase_flash']
        self.thread.state = states.ERASE
        self.thread.command = command
        self.thread.start()

    def writeFlash(self):
        binFilePath = self.optBinDir
        try:
            assert(os.path.exists(binFilePath) == True)
        except:
            self.resultTextBrowser.append('E: '+binFilePath+' is error')
            return False
        command = ['--chip', 'esp32', '--port', str(self.port), '--baud', str(self.BAUD),\
            '--before', 'default_reset', '--after', 'hard_reset', 'write_flash', '0x0000', binFilePath]
        self.thread.state = states.WRITE
        self.thread.command = command
        self.thread.start()

    def verifyFlash(self):
        choose = self.optChoose
        cmd = ['--chip', 'esp32', '--port', str(self.port), '--baud', str(self.BAUD), \
            'verify_flash']
        configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        yamlConfig = yaml.load(configFile, yaml.Loader)
        configFile.close()
        for binDir, offset in self.OriBinDict[choose].items():
            if yamlConfig['childrenForm'][binDir] == '':
                continue
            try:
                assert(os.path.exists(yamlConfig['childrenForm'][binDir])==True)
            except:
                self.resultTextBrowser.append('E: '+ yamlConfig['childrenForm'][binDir]+ ' is error')
                return False
            cmd.append(yamlConfig['childrenForm'][offset])
            cmd.append(yamlConfig['childrenForm'][binDir])
        self.thread.state = states.VERIFY
        self.thread.command = cmd
        self.thread.start()

    def flashProcess(self):
        self.resultTextBrowser.clear()
        self.resultBrowser.clear()
        self.resultBrowser.setHtml("<img src='./LOADING.png'>")
        self.flash_thread(states.CHECK)
        return False

    @pyqtSlot()
    def on_custFlashBtn_clicked(self):
        self.optChoose = self.CUST_FLASH

        configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        yamlConfig = yaml.load(configFile, yaml.Loader)
        configFile.close()

        # self.optBinDir = self.custFwEdit.text()
        self.optBinDir = yamlConfig[self.flashSet._winName]["custFwEdit"]
        self.flashProcess()

    @pyqtSlot()
    def on_pieFlashBtn_clicked(self):
        self.optChoose = self.TEST_FLASH

        configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        yamlConfig = yaml.load(configFile, yaml.Loader)
        configFile.close()
        
        # self.optBinDir = self.pieFwEdit.text()
        self.optBinDir = yamlConfig[self.flashSet._winName]["pieFwEdit"]
        self.flashProcess()

    def searchVarPort(self):
        varifyPort = QSerialPortInfo.availablePorts()
        if varifyPort == None:
            return
        self.resultTextBrowser.clear()
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
        self.configFile.close()

        defConfigFile = codecs.open(self._defaultYamlName, 'r', encoding='utf-8')           
        defConfig = yaml.load(defConfigFile, yaml.Loader)
        defConfigFile.close()

        for winName, secondDict in defConfig.items():
            for editLine in secondDict.keys():
                if editLine not in self.config[winName].keys():
                    shutil.copyfile(self._defaultYamlName, self._userYamlName)
                    self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
                    self.config = yaml.load(self.configFile, yaml.Loader)
                    self.configFile.close()

    def childShow(self):
        
        self.child.show()
        self._disableBtn()
        self.child.run()

    def flashSetShow(self):
        self.flashSet.show()
        self.flashSet.run()

    def run(self):
        self.loadYaml()

class flashWorkerThread(QThread):
    finish = pyqtSignal(Enum, str)
    state = states.CHECK
    command = None

    def __init__(self):
        return super().__init__()

    def run(self):
        try:
            esptool.main(self.command)
        except Exception as e:
            print("E:", e)
            self.finish.emit(self.state, "FAIL")
            return
    
        self.finish.emit(self.state, 'PASS')

class ChildrenForm(QWidget, Ui_Form):
    CloseSignal = pyqtSignal()
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

        self.loadYaml()

        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(),self.height())
        
        self.custBinDir_1.setReadOnly(True)
        self.custBinDir_2.setReadOnly(True)
        self.custBinDir_3.setReadOnly(True)
        self.custBinDir_4.setReadOnly(True)

        self.pieBinDir_1.setReadOnly(True)
        self.pieBinDir_2.setReadOnly(True)
        self.pieBinDir_3.setReadOnly(True)
        self.pieBinDir_4.setReadOnly(True)
        
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
        # self.close()
        self._closeWin()

    def _discard(self):
        # self.close()
        self._closeWin()

    def _closeWin(self):
        self.close()
        self.CloseSignal.emit()

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
        self.configFile.close()

    def run(self):
        self.setWin()

class EmittingStream(QObject):
    textWritten = pyqtSignal(str)
    
    def write(self, text):
        self.textWritten.emit(str(text))
    
    def flush(self):
        pass

class FwSetForm(QWidget, Ui_flashSetForm):
    def __init__(self, *args, **kwargs):
        super(FwSetForm, self).__init__()
        self.setupUi(self)
        self._defaultYamlName = 'configDefault.yml'
        self._userYamlName = 'configUser.yml'

        self._winName = 'mainForm'
        self._winEditDict = {
            self.custFwEdit: 'custFwEdit',
            self.pieFwEdit: 'pieFwEdit',
        }

        self.loadYaml()

        self.pieFwEdit.setReadOnly(True)
        self.custFwEdit.setReadOnly(True)

        self.pieFwOptBtn.clicked.connect(self._openDir)
        self.custFwOptBtn.clicked.connect(self._openDir)

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
        configFileEdit = codecs.open(self._userYamlName, 'w', encoding='utf-8')
        data = self.config
        data[winName][key] = value
        data.update()
        yaml.dump(data, configFileEdit, yaml.SafeDumper)
        configFileEdit.close()

    def _openDir(self):
        btn_dict = {self.custFwOptBtn: self.custFwEdit, self.pieFwOptBtn: self.pieFwEdit}
        assert(self.sender() in btn_dict.keys())
        file, ok= QFileDialog.getOpenFileName(self, "Open", "./", "Binary Files(*.bin)")
        btn_dict[self.sender()].setText(file)
        # self.editYaml(self._winName, self._winEditDict[btn_dict[self.sender()]], file)

    def _setWin(self):
        for key, file in self._winEditDict.items():
            key.setText(self.config[self._winName][file])

    def loadYaml(self):
        if os.path.exists(self._userYamlName) == False:
            shutil.copyfile(self._defaultYamlName, self._userYamlName)
        self.configFile = codecs.open(self._userYamlName, 'r', encoding='utf-8')
        self.config = yaml.load(self.configFile, yaml.Loader)
        self.configFile.close()
    
    def run(self):
        self._setWin()

def main():
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.run()
    myWin.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
    