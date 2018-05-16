#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 10:05
@author: 柴顺进
@file: 06rabbit.py 
@software:rongda
@note: 第一个月初有一对兔子
"""  
def sum2(num):
    # map1 = {1:1, 2:1, 3:2, 4:3, 5:5}
    list1 = [1]*num
    print(len(list1))
    list1[1] = 1
    print(list1)
    for i in range(0,num-2):
        list1[i+2] = list1[i]+list1[i+1]
    print(list1[num-1])
    return list1[num-1]
sum2(21)

