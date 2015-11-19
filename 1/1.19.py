# -*- coding: utf-8 -*-
__author__ = '594829'
# 同时对数据做转换和换算

# 使用生成器表达式
nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums)
print(s)

# Detemine if any .py files exist in a directory
import os
files = os.listdir('dirname')
if any(name.endswith('.py') for name in files):
	print('There be python!')
else:
	print('Sorry, no python.')
