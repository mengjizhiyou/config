# Read .xml and .json file and make them more advanced

## Config.xml

```python
from read_xml import get_config

config = get_config()
print(config)
# {'table3': 'config', 'table2': '1234', 'table1': '1000'}
```



## Config.json

```python
from read_json import Config

config = Config()
print(config.__dict__)
# {'table1': 1000, 'table2': 1234, 'table3': 'config'}
hasattr(config, 'table1')
getattr(config, 'table1')
```



