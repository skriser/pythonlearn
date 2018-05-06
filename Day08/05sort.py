#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 13:29
@author: 柴顺进
@file: 05sort.py 
@software:rongda
@note: 排序
"""  
import random

list1 = []

for i in range(20):
    list1.append(random.randint(1, 100))
print list1
list1.sort()
print list1

list2 = [4, 5, 3, 2, 10, 7]
# 冒泡排序：前后相比，把大的先升到最后一位
for i in range(len(list2)):
    for j in range(len(list2)-i-1):
        if list2[j] > list2[j+1]:
            list2[j], list2[j+1] = list2[j+1], list2[j]
        print list2






# for i in len(list2):
#     while i<len(list2)/2:
#         if list2[i] > list2[len(list2)/2]:
#             list2[i], list2[len(list2)/2] = list2(len(list2)/2), list2[i]




