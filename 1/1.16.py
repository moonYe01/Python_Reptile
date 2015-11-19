__author__ = '594829'
# -*- coding: utf-8 -*-
# 筛选序列中的元素

# 列表推导式
mylist = [1, 4, -5, 10, -7, 2, 3 ,-1]

print([n for n in mylist if n > 0])
print([n for n in mylist if n < 0])

#生成器表达式
pos = (n for n in mylist if n > 0)
for x in pos:
	print(x)

# 内建filter函数，本身创建了一个迭代器
values = ['1', '2', '-3', '-', '4', 'N/A', '5']

def  is_int(val):
	try:
		x = int(val)
		return True
	except ValueError:
		return False

ivals = list(filter(is_int, values))
print(ivals)

address = [
		'5412 N CLARK',
		'5148 N CLARK',
		'5800 E 58TH',
		'2122 N CLARK',
		'5645 N RAVENSWOOD',
		'1060 W ADDISON',
		'4801 N BORADWAY',
		'1039 W GRANVILLE'
]

counts = [0,3,10,4,1,7,6,1]

from itertools import compress
more5 = [n > 5 for n in counts]
print(list(compress(address, more5)))
