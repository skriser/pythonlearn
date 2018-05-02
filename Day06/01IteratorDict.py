#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 9:17
@author: 柴顺进
@file: 01IteratorDict.py 
@software:rongda
@note: 用for循环去读取字典
"""

dict1 = {'apple': 1, 'orange': 2, 'banana': 3}

# 字典是无序的，不能通过下表进行读取
for i in dict1:
    print i, dict1[i]

