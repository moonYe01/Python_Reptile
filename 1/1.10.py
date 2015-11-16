__author__ = '594829'
# -*- coding: utf-8 -*-


# 从序列中移除重复项且保持元素间顺序不变
# hashable
# def dedpue(items):
# 	seen = set()
# 	for item in items:
# 		if item not in seen:
# 			yield item
# 			seen.add(item)

# a = [1,2,5,3,7,4,5,9,2,4,1]
# print(list(dedpue(a)))

# 不可哈希对象

# def dedupe(items, key=None):
# 	seen = set()
# 	for item in items:
# 		val = item if key is None else key(item)
# 		if val not in seen:
# 			yield item
# 			seen.add(val)
#
# a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
# print(list(dedupe(a,key=lambda d: (d['x'],d['y']))))

#去除重复项
a = [1,2,45,2,7,4,9,4,6,0,8,7]

# a = [{'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
print(set(a))
