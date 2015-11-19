__author__ = '594829'
# -*- coding: utf-8 -*-

# 利用公共键对字典列表进行排序:itemgetter函数
rows = [
	{'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
	{'fname': 'David', 'lname': 'Beazleys', 'uid': 1002},
	{'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
	{'fname': 'Big', 'lname': 'Jones', 'uid': 1004},
]

from operator import itemgetter

rows_by_fname = sorted(rows, key=itemgetter('fname'))
rows_by_uid = sorted(rows, key=itemgetter('uid'))
rows_by_lfname = sorted(rows, key=itemgetter('lname','fname'))

minr = min(rows, key=itemgetter('uid'))
maxr = max(rows, key=itemgetter('uid'))


print(rows_by_fname)
print(rows_by_uid)
print(rows_by_lfname)

print(minr)
print(maxr)

