#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 10:22
@author: 柴顺进
@file: 07while.py 
@software:rongda
@note: 兔子生到100万要多久
"""


def sum2(nums):
    # map1 = {1:1, 2:1, 3:2, 4:3, 5:5}
    list1 = [1]*nums
    for i in range(0, nums-2):
        list1[i+2] = list1[i]+list1[i+1]
    return list1[nums-1]*2


def judeMonth():
    month = 3
    while sum2(month) < 1000000:
        month += 1
    return month


print(judeMonth())