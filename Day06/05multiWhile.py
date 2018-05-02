#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 10:35
@author: 柴顺进
@file: 05multiWhile.py 
@software:rongda
@note: 输出直角三角形
"""  
# i = 1
# while i < 6:
#     j = 6
#     while j > i:
#         print '%-s'%'*',
#         j -= 1
#     print
#     i += 1

for i in range(1, 6):
    for j in range(i):
        print "%s"%("*"),
    print

# 列推导式更高效快速
list1 = [i for i in range(1, 11)]
a = [i**2 for i in range(1, 11)]
b = [i for i in range(1, 10, 2)]
print b
c1 = [i for i in range(2, 11, 2)]
c = [i for i in range(2, 11) if i % 2 == 0]
print c
print c1

# 把大写英文变成小写
print [x.lower() for x in list('ABCDEF')]
print [x.upper() for x in 'adbcef']

# 字典的推导式
print {i: i+1 for i in range(4)}
print {i: j for i, j in zip(range(3), 'abc')}

