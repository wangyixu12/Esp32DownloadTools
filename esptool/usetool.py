'''
@Author: Yixu Wang
@Date: 2019-08-05 09:35:11
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-06 10:55:45
@Description: file content
'''
import esptool
import os
# import sys
import time
import difflib
import copy
# from pynput import keyboard

outputFile = 'output/output.bin'

inputDir = 'input/'

bootFileDir = inputDir + 'bootloader.bin'
partFileDir = inputDir + 'my_partitions.bin'
appFileDir = inputDir + 'oralb_turing_seagate.bin'
otaFileDir = inputDir + 'ota_data_initial.bin'

bootSize = os.path.getsize(bootFileDir)
partSize = os.path.getsize(partFileDir)
appSize = os.path.getsize(appFileDir)
otaSize = os.path.getsize(otaFileDir)

defaultCommand = ['--baud', '1152000', 'read_flash', '', '', 'output/output.bin']
bootCommand = copy.deepcopy(defaultCommand)
bootCommand[3] = '0x1000'
bootCommand[4] = str(bootSize)

partCommand = copy.deepcopy(defaultCommand)
partCommand[3] = '0x8000'
partCommand[4] = str(partSize)

appCommand = copy.deepcopy(defaultCommand)
appCommand[3] = '0x10000'
appCommand[4] = str(appSize)

otaCommand = copy.deepcopy(defaultCommand)
otaCommand[3] = '0xd000'
otaCommand[4] = str(otaSize)

def diff_is(fromFile, toFile):
    ret = False
    aFile = open(fromFile, 'r').read().splitlines(True)
    bFile = open(toFile, 'r').read().splitlines(True)

    diff = difflib.context_diff(aFile, bFile, fromfile=fromFile, tofile=toFile, n=0, lineterm='\n')
    result = ''.join(diff)
    # print(result)
    if result == '':
        ret = True
    return ret

def verify(command, fileDir):
    esptool.main(command)
    if diff_is(fileDir, outputFile) == False:
        print('\033[1;31;40m FAIL!!! FAIL!!! FAIL!!! \033[0m')
        time.sleep(5)        
        os._exit(0)
        # return False
    else:
        print("PASS")
        return True

def main():
    # filePath = 'input/50FW-000X0-P1C-0200-121_0x6000AD52.bin'
    # fsize = os.path.getsize(filePath)
    # print(fsize)
    # command = defaultCommand
    # print('Using command %s' % ''.join(command))
    # esptool.main(command)

    # verify(bootCommand, bootFileDir)
    verify(partCommand, partFileDir)
    verify(appCommand, appFileDir)
    verify(otaCommand, otaFileDir)
    print('\033[1;33;40m PASS!!! PASS!!! PASS!!! \033[0m')
    time.sleep(5)


    # if verify(bootCommand, bootFileDir) == False:
        # print('\033[1;31;40m FAIL!!! FAIL!!! FAIL!!! \033[0m')

    # esptool.main(partCommand)
    # if diff_is(partFileDir, outputFile) == False:
    #     print('Failure!')
    # else:
    #     print("PASS")
    # esptool.main(appCommand)
    # esptool.main(otaCommand)



defaultVerify = ["--chip", 'esp32', '--port', 'dev/ttyUSB0', '--baud', '1152000', "verify_flash --diff=yes", "0x0", ""]

def on_press(key):
    if key == keyboard.Key.esc:
        return false
    else:
        pass

if __name__ == '__main__':
    # while(True):
    main()
        # print('\033[7;37;40m Quit: press "esc" key, Continue: press other keys \033[7m')
        # with keyboard.Listener(on_press=on_press) as listener:
        #     listener.join()
    
