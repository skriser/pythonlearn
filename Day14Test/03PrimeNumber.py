#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 9:48
@author: 柴顺进
@file: 03PrimeNumber.py 
@software:rongda
@note: 输出1-100内的质数，类似于2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,
"""  
for i in range(2,100):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
        print(i,end=',')
