import os
import sys
import xml.etree.ElementTree as ET
from itertools import chain
from collections import ChainMap

code_path = os.path.dirname(os.path.abspath(__file__))


def get_config():
    path = os.path.join(code_path, 'config.xml')
    tree = ET.parse(path)
    root = tree.getroot()
    tb1, tb2, tb3 = [root[0][i].text for i in range(3)]
    return tb1, tb2, tb3


config = get_config()
print(config)
# ('1000', '1234', 'config')



# -------------------------------------------
# 进阶，方法二


def get_config():
    path = os.path.join(code_path, 'config.xml')
    tree = ET.parse(path)
    root = tree.getroot()
    config = list(map(lambda i: list(map(lambda j: {j.tag: j.text}, i)), root))
    config = list(chain.from_iterable(config))
    config = dict(ChainMap(*config))
    return config


config = get_config()
print(config)
# {'table3': 'config', 'table2': '1234', 'table1': '1000'}