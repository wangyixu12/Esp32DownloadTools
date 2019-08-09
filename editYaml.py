'''
@Author: Yixu Wang
@Date: 2019-08-08 16:10:53
@LastEditors: Yixu Wang
@LastEditTime: 2019-08-09 09:30:47
@Description: Yaml 的操作
'''
import yaml
import os
import codecs

class optYaml(object):
    def __init__(self, dir = './output/', filename = "configure.yml", *args):
        self._filename = dir + filename
        self._dir = dir
        self._mkdir()
        self._file = open(self._filename, 'a+')
        self.myYaml = yaml.load(self._file, Loader=yaml.FullLoader)

    def _mkdir(self):
        if not os.path.exists(self._dir):
            os.makedirs(self._dir)

    def write(self):
        pass
    
    def read(self):
        pass

    def close(self):
        self._file.close()
    # def 


with  codecs.open('yaml name', 'r', encoding='utf-8') as file:
    config = yaml.load(file, yaml.Loader)
    print(config)

with codecs.open('yaml file', 'w', encoding='utf-8') as config_yaml_file:
    data = config
    data['developer']['back'] = 6969
    data.update()
    yaml.dump(data, config_yaml_file, yaml.SafeDumper)
    config_yaml_file.close()