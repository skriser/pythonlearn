#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 13:19
@author: 柴顺进
@file: 04SetRange.py 
@software:rongda
@note: range() 函数在set中的应用
"""  

print range(4)
print range(5, 10)
print range(1, 10, 2)

# str() list() tuple() dict() set() 里面的数据都可以通过range()生成
print dict(range(4))

