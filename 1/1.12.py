__author__ = '594829'
# -*- coding:utf-8 -*-

# 查找序列中出现次数最多的元素
words = [
	'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
	'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
	'eyes', "don't", 'look', 'around', 'the', 'the', 'eyes', 'look', 'into',
	'my', 'eyes', "you're", 'under'
]

from collections import Counter
# # 统计序列中的元素
# word_counts = Counter(words)
# # 元素出现次数最多的前3位
# top_three = word_counts.most_common(3)
# print(top_three)


morewords = ['why', 'are', 'you', 'not', 'looking', 'in', 'my', 'eyes']

a = Counter(words)
b = Counter(morewords)

print(a)
print(b)

# combine counts
c = a + b
print(c)

# Substract counts
s = a - b
print(s)

