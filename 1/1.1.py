

__author__ = '594829'


# def drop_first_last(grades):
#     first,*middle,last = grades
#     return avg(middle)


# grades = [2,4,7,5,3,1,8,4,3]
# drop_first_last(grades)

#
records = [
    ('foo',1,2),
    ('bar','hello'),
    ('foo',3,4),
]

def do_foo(x,y):
    print('foo',x,y)

def do_bar(s):
    print('bar',s)


for tag,*args in records:
    if tag == 'foo':
        do_foo(*args)
    elif tag == 'bar':
        do_bar(*args)
