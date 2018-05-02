#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 13:52
@author: 柴顺进
@file: 08continuedemo.py 
@software:rongda
@note: 
"""  
# 求1-100以内的质数：质数是指只能被1和本身整除的数,同时质数是大于1的自然数
# for i in range(0, 100):
#     j = 1
#     while j < i:
#         if i % j == 0 and j != 1:
#             break
#         if j+1 == i:
#             print i,
#         j += 1


for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print i,
