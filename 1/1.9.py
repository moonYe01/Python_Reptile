# -*- coding: utf-8 -*-
__author__ = '594829'

# 找到两个字典中相同的地方（值，键）

a = {
	'x': 1,
	'y': 2,
	'z': 3
}

b = {
	'w': 10,
	'x': 11,
	'y': 2
}

# Find keys in common
common = a.keys() & b.keys()  # { 'x', 'y' }

# Find keys in a that are not in b
diff = a.keys() - b.keys()  # {'z'}

# Find (key,value) pairs in common
same = a.items() & b.items()  # {('y',2)}

# Make a new dictionary with certain keys removed
c = {key:a[key] for key in a.keys() - {'z','w'}}  # {('x',1),('y',2)}

print(common)   # {'x', 'y'}
print(diff)		# {'z'}
print(same)		# {('y',2)}
print(c)		# {('x',1),('y',2)}

