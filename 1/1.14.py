__author__ = '594829'
# -*- coding: utf-8 -*-

# 对原生不支持比较操作的对象进行排序

#第一种方法利用lambda表达式
class User:
	def __init__(self,user_id):
		self.user_id = user_id
	def __repr__(self):
		return 'User({})'.format(self.user_id)

users = [User(23), User(3), User(99)]
sortUser = sorted(users, key=lambda u: u.user_id)
print(sortUser)

# 第二种方法利用attrgetter()
from operator import attrgetter
arrtUser = sorted(users, key=attrgetter('user_id'))
print(arrtUser)

minUser = min(users, key=attrgetter('user_id'))
maxUser = max(users, key=attrgetter('user_id'))
print(minUser)
print(maxUser)