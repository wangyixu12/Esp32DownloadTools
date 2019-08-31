'''
@Author: Yixu Wang
@Date: 2019-08-06 14:12:40
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-30 17:45:17
@Description: The ESP32 Download tool GUI
'''
import os
import sys
import codecs
import shutil
from enum import Enum
import yaml

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QThread
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtCore import QObject
from PyQt5.QtCore import Qt
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QTextCursor

import esptool

from Ui_mainForm import Ui_MainWindow
from Ui_childrenForm import Ui_Form
from Ui_flashSetForm import Ui_flashSetForm

class States(Enum):
    ''' State machine's states enumeration.
    '''
    CHECK = 0
    ERASE = 1
    WRITE = 2
    VERIFY = 3
    RESULT = 4

class MyMainWindow(QMainWindow, Ui_MainWindow):
    ''' Main window's class
    '''

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
        self._default_yaml_name = './config/configDefault.yml'
        self._user_yaml_name = './config/configUser.yml'
        self.opt_choose = None
        self.opt_bin_dir = None
        self.cur_port_location = None
        self.config = None

        self.ver_bin_dict = {
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
            States.CHECK.value : self.check_conf,
            States.ERASE.value : self.erase_flash,
            States.WRITE.value : self.write_flash,
            States.VERIFY.value : self.verify_flash,
            States.RESULT.value : self._disp_result
        }
        self.port = ''
        sys.stdout = EmittingStream(textWritten=self.output_written)

        self.child = ChildrenForm()
        self.child.CloseSignal.connect(self._enable_btn)

        self.flash_set = FwSetForm()
        self.flash_set.CloseSignal.connect(self._enable_btn)

        self.thread = FlashWorkerThread()
        self.thread.finish.connect(self.flash_thread)

        self.resultTextBrowser.setReadOnly(True)
        self.resultBrowser.setReadOnly(True)

        self.actVeriFw.triggered.connect(self.child_show)
        self.actFlashFw.triggered.connect(self.flash_set_show)
        self.searchPortBtn.clicked.connect(self.search_var_port)
        self.portComBox.currentIndexChanged.connect(self.select_com_port)

    def __del__(self):
        sys.stdout = sys.__stdout__

    def _enable_btn(self):
        self.pieFlashBtn.setEnabled(True)
        self.custFlashBtn.setEnabled(True)
        self.searchPortBtn.setEnabled(True)
        self.actVeriFw.setEnabled(True)
        self.actFlashFw.setEnabled(True)

    def _disable_btn(self):
        self.pieFlashBtn.setEnabled(False)
        self.custFlashBtn.setEnabled(False)
        self.searchPortBtn.setEnabled(False)
        self.actVeriFw.setEnabled(False)
        self.actFlashFw.setEnabled(False)

    def output_written(self, text):
        cursor = self.resultTextBrowser.textCursor()
        cursor.movePosition(QTextCursor.End)
        cursor.insertText(text)
        self.resultTextBrowser.setTextCursor(cursor)
        self.resultTextBrowser.ensureCursorVisible()

    def _disp_result(self, result):
        # if result == 'FAIL':
        self._enable_btn()
        self.resultBrowser.setHtml("<img src='./img/"+result+".png'>")

    def flash_thread(self, opt, data=None):
        # print(opt, data)
        if data == 'FAIL':
            self.resultTextBrowser.append(opt.name + ' --> FAIL\n')
            self._transitions[States.RESULT.value]("FAIL")
            return
        elif data == 'PASS':
            self.resultTextBrowser.append(opt.name + ' --> PASS\n')
        if opt == States.VERIFY:
            self._transitions[opt.value + 1](data)
        elif opt == States.CHECK:
            self._transitions[opt.value]()
        else:
            self._transitions[opt.value + 1]()

    def check_conf(self):
        choose = self.opt_choose
        assert(choose == self.CUST_FLASH) | (choose == self.TEST_FLASH)
        ret = True
        config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        yaml_config = yaml.load(config_file, yaml.Loader)
        config_file.close()

        if self.port == '':
            self.resultTextBrowser.setPlainText(self.ERASE_FAIL+"Err: Serial port isn't set\n")
            ret = False

        if choose == self.TEST_FLASH:
            if yaml_config["mainForm"]["pieFwEdit"] == '':
                self.resultTextBrowser.append(self.WRITE_FAIL+"Err: Tester firmware isn't set\n")
                ret = ret & False

        elif choose == self.CUST_FLASH:
            if yaml_config["mainForm"]["custFwEdit"] == '':
                self.resultTextBrowser.append(self.WRITE_FAIL+"Err: Customer firmware isn't set\n")
                ret = ret & False

        is_content = False
        for bin_dir, offset in self.ver_bin_dict[choose].items():
            is_content = is_content | bool(yaml_config[self.child.win_name][bin_dir])
            if (
                    bool(yaml_config[self.child.win_name][bin_dir]) !=
                    bool(yaml_config[self.child.win_name][offset])
            ):
                self.resultTextBrowser.append(self.VARI_FAIL + 'Err: Verify bin file setting error')
                ret = ret & False
                break
        else:
            if not is_content:
                self.resultTextBrowser.append(self.VARI_FAIL+'Err: Verify bin file setting error\n')
                ret = ret & False

        if ret:
            # self.flash_thread(States.ERASE)
            self.erase_flash()
        else:
            self.flash_thread(States.RESULT, "FAIL")

    def erase_flash(self):
        command = ['--port', str(self.port), 'erase_flash']
        self.thread.state = States.ERASE
        self.thread.command = command
        self.thread.start()

    def write_flash(self):
        bin_file_path = self.opt_bin_dir
        try:
            assert os.path.exists(bin_file_path)
        except OSError:
            self.resultTextBrowser.append('Err: Flash bin path is error.')
            self.flash_thread(States.WRITE, "FAIL")
            return False
        except Exception as e:
            self.resultTextBrowser.append('Err: Flash bin path is error.\n'+"Err: "+str(e))
            self.flash_thread(States.WRITE, "FAIL")
            return False
        command = ['--chip', 'esp32', '--port', str(self.port), '--baud', str(self.BAUD),\
                    '--before', 'default_reset', '--after', 'hard_reset', 'write_flash',\
                    '0x0000', bin_file_path]
        self.thread.state = States.WRITE
        self.thread.command = command
        self.thread.start()

    def verify_flash(self):
        choose = self.opt_choose
        cmd = ['--chip', 'esp32', '--port', str(self.port), '--baud', str(self.BAUD), \
            'verify_flash']
        config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        yaml_config = yaml.load(config_file, yaml.Loader)
        config_file.close()
        for bin_dir, offset in self.ver_bin_dict[choose].items():
            if yaml_config['childrenForm'][bin_dir] == '':
                continue
            try:
                assert os.path.exists(yaml_config['childrenForm'][bin_dir])
            except OSError:
                self.resultTextBrowser.append('Err: Verify bin file is error')
                self.flash_thread(States.VERIFY, "FAIL")
                return False
            except Exception as e:
                self.resultTextBrowser.append('Err: '+str(e))
                self.flash_thread(States.VERIFY, "FAIL")
                return False
            cmd.append(yaml_config['childrenForm'][offset])
            cmd.append(yaml_config['childrenForm'][bin_dir])
        self.thread.state = States.VERIFY
        self.thread.command = cmd
        self.thread.start()

    def flash_process(self):
        self.resultTextBrowser.clear()
        self.resultBrowser.clear()
        self.resultBrowser.setHtml("<img src='./img/LOADING.png'>")
        self.BAUD = self.baudComboBox.currentText()
        self.flash_thread(States.CHECK)
        return False

    @pyqtSlot()
    def on_custFlashBtn_clicked(self):
        self._disable_btn()
        self.opt_choose = self.CUST_FLASH

        config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        yaml_config = yaml.load(config_file, yaml.Loader)
        print(yaml_config)
        config_file.close()

        # self.opt_bin_dir = self.custFwEdit.text()
        self.opt_bin_dir = yaml_config[self.flash_set.win_name]["custFwEdit"]
        self.flash_process()

    @pyqtSlot()
    def on_pieFlashBtn_clicked(self):
        self._disable_btn()
        self.opt_choose = self.TEST_FLASH

        config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        yaml_config = yaml.load(config_file, yaml.Loader)
        config_file.close()

        # self.opt_bin_dir = self.pieFwEdit.text()
        self.opt_bin_dir = yaml_config[self.flash_set.win_name]["pieFwEdit"]
        self.flash_process()

    def search_var_port(self):
        varify_port = QSerialPortInfo.availablePorts()
        if varify_port is None:
            return
        self.resultTextBrowser.clear()
        self.portComBox.clear()
        for ser_port_info in varify_port:
            if 'USB' not in ser_port_info.portName():
                continue
            self.portComBox.addItem(ser_port_info.portName())

    def select_com_port(self):
        cur_port = QSerialPortInfo(self.portComBox.currentText())
        self.cur_port_location = cur_port.systemLocation()
        self.port = self.cur_port_location

    def load_yaml(self):
        if not os.path.exists(self._user_yaml_name):
            shutil.copyfile(self._default_yaml_name, self._user_yaml_name)
        config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        self.config = yaml.load(config_file, yaml.Loader)
        config_file.close()

        def_config_file = codecs.open(self._default_yaml_name, 'r', encoding='utf-8')
        def_config = yaml.load(def_config_file, yaml.Loader)
        def_config_file.close()

        for win_name, second_dict in def_config.items():
            for edit_line in second_dict.keys():
                if edit_line not in self.config[win_name].keys():
                    shutil.copyfile(self._default_yaml_name, self._user_yaml_name)
                    config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
                    self.config = yaml.load(config_file, yaml.Loader)
                    config_file.close()

    def child_show(self):
        self.child.show()
        self._disable_btn()
        self.child.run()

    def flash_set_show(self):
        self.flash_set.show()
        self._disable_btn()
        self.flash_set.run()

    def run(self):
        self.load_yaml()

class FlashWorkerThread(QThread):
    ''' The thread for GUI
    '''
    finish = pyqtSignal(Enum, str)
    state = States.CHECK
    command = None

    def run(self):
        try:
            esptool.main(self.command)
        except Exception as e:
            print(str(self.state.name)+" Error:"+str(e))
            self.finish.emit(self.state, "FAIL")
            return

        self.finish.emit(self.state, 'PASS')

class ChildrenForm(QWidget, Ui_Form):
    CloseSignal = pyqtSignal()
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)
        self._default_yaml_name = 'config/configDefault.yml'
        self._user_yaml_name = 'config/configUser.yml'

        self.win_name = 'childrenForm'
        self._win_edit_dict = {
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


        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())

        self.custBinDir_1.setReadOnly(True)
        self.custBinDir_2.setReadOnly(True)
        self.custBinDir_3.setReadOnly(True)
        self.custBinDir_4.setReadOnly(True)

        self.pieBinDir_1.setReadOnly(True)
        self.pieBinDir_2.setReadOnly(True)
        self.pieBinDir_3.setReadOnly(True)
        self.pieBinDir_4.setReadOnly(True)

        self.custBinOptBtn_1.clicked.connect(self.open_dir)
        self.custBinOptBtn_2.clicked.connect(self.open_dir)
        self.custBinOptBtn_3.clicked.connect(self.open_dir)
        self.custBinOptBtn_4.clicked.connect(self.open_dir)

        self.pieBinOptBtn_1.clicked.connect(self.open_dir)
        self.pieBinOptBtn_2.clicked.connect(self.open_dir)
        self.pieBinOptBtn_3.clicked.connect(self.open_dir)
        self.pieBinOptBtn_4.clicked.connect(self.open_dir)

        self.binFileComfirm.button(self.binFileComfirm.Save).clicked.connect(self._save)
        self.binFileComfirm.button(self.binFileComfirm.Discard).clicked.connect(self._discard)

    def _save(self):
        for edit_key in self._win_edit_dict:
            text = edit_key.text()
            self.edit_yaml(self.win_name, self._win_edit_dict[edit_key], text)
        # self.close()
        self._close_win()

    def _discard(self):
        # self.close()
        self._close_win()

    def _close_win(self):
        self.close()
        self.CloseSignal.emit()

    def edit_yaml(self, win_name, key, value):
        # self.config = yaml.load(self.config_file, yaml.Loader)
        config_file_edit = codecs.open(self._user_yaml_name, 'w', encoding='utf-8')
        data = self.config
        data[win_name][key] = value
        data.update()
        yaml.dump(data, config_file_edit, yaml.SafeDumper)
        config_file_edit.close()

    def open_dir(self):
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
        assert self.sender() in btn_dict.keys()
        file, ok = QFileDialog.getOpenFileName(self, "Open", './', 'Binary Files(*.bin)')
        btn_dict[self.sender()].setText(file)
        # self.edit_yaml(self.win_name, self._win_edit_dict[btn_dict[self.sender()]], file)

    def set_win(self):
        for key, file in self._win_edit_dict.items():
            key.setText(self.config[self.win_name][file])

    def load_yaml(self):
        if not os.path.exists(self._user_yaml_name):
            shutil.copyfile(self._default_yaml_name, self._user_yaml_name)
        self.config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        self.config = yaml.load(self.config_file, yaml.Loader)
        self.config_file.close()

    def run(self):
        self.load_yaml()
        self.set_win()

class EmittingStream(QObject):
    textWritten = pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass

class FwSetForm(QWidget, Ui_flashSetForm):
    CloseSignal = pyqtSignal()
    def __init__(self):
        super(FwSetForm, self).__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.WindowMinimizeButtonHint)
        self.setFixedSize(self.width(), self.height())
        self._default_yaml_name = 'config/configDefault.yml'
        self._user_yaml_name = 'config/configUser.yml'

        self.win_name = 'mainForm'
        self._win_edit_dict = {
            self.custFwEdit: 'custFwEdit',
            self.pieFwEdit: 'pieFwEdit',
        }


        self.pieFwEdit.setReadOnly(True)
        self.custFwEdit.setReadOnly(True)

        self.pieFwOptBtn.clicked.connect(self._open_dir)
        self.custFwOptBtn.clicked.connect(self._open_dir)

        self.binFileComfirm.button(self.binFileComfirm.Save).clicked.connect(self._save)
        self.binFileComfirm.button(self.binFileComfirm.Discard).clicked.connect(self._discard)

    def __del__(self):
        self.close()
        self.CloseSignal.emit()

    def _save(self):
        for edit_key in self._win_edit_dict:
            text = edit_key.text()
            self.edit_yaml(self.win_name, self._win_edit_dict[edit_key], text)
        # self.close()
        self._close_win()

    def _discard(self):
        # self.close()
        self._close_win()

    def _close_win(self):
        self.close()
        self.CloseSignal.emit()

    def edit_yaml(self, win_name, key, value):
        config_file_edit = codecs.open(self._user_yaml_name, 'w', encoding='utf-8')
        data = self.config
        data[win_name][key] = value
        data.update()
        yaml.dump(data, config_file_edit, yaml.SafeDumper)
        config_file_edit.close()

    def _open_dir(self):
        btn_dict = {self.custFwOptBtn: self.custFwEdit, self.pieFwOptBtn: self.pieFwEdit}
        assert self.sender() in btn_dict.keys()
        file, ok = QFileDialog.getOpenFileName(self, "Open", "./", "Binary Files(*.bin)")
        btn_dict[self.sender()].setText(file)
        # self.edit_yaml(self.win_name, self._win_edit_dict[btn_dict[self.sender()]], file)

    def _set_win(self):
        for key, file in self._win_edit_dict.items():
            key.setText(self.config[self.win_name][file])

    def load_yaml(self):
        if not os.path.exists(self._user_yaml_name):
            shutil.copyfile(self._default_yaml_name, self._user_yaml_name)
        self.config_file = codecs.open(self._user_yaml_name, 'r', encoding='utf-8')
        self.config = yaml.load(self.config_file, yaml.Loader)
        self.config_file.close()

    def run(self):
        self.load_yaml()
        self._set_win()

def main():
    app = QApplication(sys.argv)
    # app.aboutToQuit.connect(app.deleteLater)
    my_win = MyMainWindow()
    my_win.run()
    my_win.show()
    app.exec_()

if __name__ == '__main__':
    main()
    