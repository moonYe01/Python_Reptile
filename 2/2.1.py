# -*- coding: utf-8 -*-
__author__ = '594829'

# 针对任意多的分隔符拆分字符串

line = 'asdf fjdk; afed, fjek,asdf,  foo'
import re
groups = re.split(r'[;,\s]\s*', line)
print(groups)

fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']

print(values)
print(delimiters)

xx = ''.join(v+d for v,d in zip(values, delimiters))
print(xx)


nonCapture = re.split(r'(?:,|;|\s)\s*',line)
print(nonCapture)