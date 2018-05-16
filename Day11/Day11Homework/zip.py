#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 9:38
@author: 柴顺进
@file: zip.py 
@software:rongda
@note: 
"""  
data = [
    ['HTML', 'CSS', 'javascript'],
    ['this is a1', '', 'this is c1'],
    ['hehe', '', '', 'haha']
]
newdata = list(zip(*data))
print(newdata)
# for i in zip(*data):
#     print(i)
