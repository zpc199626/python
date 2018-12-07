#/usr/bin/env python
#-*- coding:utf-8 -*-
import json
date = {'name':'中国'}
"""将字典改为json数据"""
date_1 = json.dumps(date)
print(date_1)
"""将json数据更改为字典"""
date_2 = json.loads(date_1)
print(date_2)