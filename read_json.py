import json
import os, sys

def get_config():
    path = os.path.join(os.path.dirname(sys.argv[0]), 'config.json')
    config = json.load(open(path, mode='r'))
    return config


config = get_config()
print(config)
# {'table3': 'config', 'table2': '1234', 'table1': '1000'}



# -------------------------------------------
# 进阶，方法二
# 改写成类的属性

class Config:
    def __init__(self):
        config = self.get_config()
        for k, v in config.items():
            # setattr(self, k, v)
            self.__setattr__(k, v)

    def get_config(self):
        path = os.path.join(os.path.dirname(sys.argv[0]), 'config.json')
        config = json.load(open(path, mode='r'))
        return config

    def __setattr__(self, name, value):
        super().__setattr__(name, value)


config = Config()
print(config.__dict__)
# {'table1': 1000, 'table2': 1234, 'table3': 'config'}
hasattr(config, 'table1')
getattr(config, 'table1')