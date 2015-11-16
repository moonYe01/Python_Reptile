__author__ = '594829'

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

p = defaultdict(set)
p['a'].add(1)
p['a'].add(2)
p['b'].add(4)

print(d)
print(p)

