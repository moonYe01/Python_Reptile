from collections import namedtuple
__author__ = '594829'
# -*- coding: utf-8 -*-

#将名称映射到序列的元素中
Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')
print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))
addr,joined = sub
print(addr)
print(joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price'])
def compute_cost(records):
	total = 0.0
	for rec in records:
		s = Stock(*rec)
		total += s.shares * s.price
	return total

print(compute_cost(Stock))