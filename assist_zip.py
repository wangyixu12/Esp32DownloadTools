'''
@Author: Yixu Wang
@Date: 2019-10-22 13:40:46
@LastEditors: Yixu Wang
@LastEditTime: 2019-10-22 14:41:59
@Version: v0.0.1
@Description: unzip file
'''
import zipfile
# import yaml
import os

def unzip(file_name, dir_name):
    '''
        unzip zip file
    '''
    zip_file = zipfile.ZipFile(file_name)
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    zip_member = zip_file.namelist()
    zip_file.extractall(dir_name, zip_member)
    zip_file.close()

if __name__ == "__main__":
    FILE_DIR = './data/50FW-000W0-P1C-0200-118_0x03F52E3D/'
    FILE_NAME = 'ubuntu_download_tool_config.zip'
    __HIDE_DIR_PATH = './.data/'
    __TESTER_DIR_NAME = __HIDE_DIR_PATH + 'tester'
    unzip(FILE_DIR+FILE_NAME, __TESTER_DIR_NAME)