__author__ = '594829'
# -*- coding: utf-8 -*-
from collections import OrderedDict
import json

# 在添加按数据时，进行字典排序
d = OrderedDict()
d['foo'] = 2
d['bar'] = 3
d['spam'] = 1
d['grok'] = 4

for key in d:
    print(key, d[key])

print(json.dumps(d))