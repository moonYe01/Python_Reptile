__author__ = '594829'
# -*- coding: utf-8 -*-

import heapq

# 在某个集合中找出最大或最小的N个元素
nums = [1,8,2,-23,7,-4,18,23,42,37,2]

print(heapq.nlargest(3,nums))
print(heapq.nsmallest(3,nums))

# 根据某个对象中的某个字段值找最大或最小的N个元素
# key 定义规则
portfolio = [
    {'name': 'IBM', 'share': 100, 'price': 91.1},
    {'name': 'AAPL', 'share': 50, 'price': 543.22},
    {'name': 'FB', 'share': 200, 'price': 21.09},
    {'name': 'HPQ', 'share': 35, 'price': 31.75},
    {'name': 'YHOO', 'share': 45, 'price': 16.35}
]

cheap = heapq.nsmallest(3, portfolio, key=lambda s: s['price'])
expensive = heapq.nlargest(3, portfolio, key=lambda s:s['price'])

print(cheap)

print(expensive)

