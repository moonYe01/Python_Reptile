__author__ = '594829'
# -*- coding:utf-8 -*-

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2,4)

print(a.start)
print(a.stop)
print(a.step)


s = 'HelloWold'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
	print(s[i])