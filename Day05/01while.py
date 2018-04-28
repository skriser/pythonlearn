#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/04/28 2018/4/28 9:14
@author: 柴顺进
@file: 01while.py 
@software:rongda
@note: while循环使用
"""  
# 一到一百能被3整除的数
num1 = 0
while num1 < 100:
    if num1 % 3 == 0:
        print num1
    num1 += 1

num2 = 0
while num2 < 99:
    print num2,
    num2 += 3

num3 = 1
while num3*3 < 100:
    print num3*3,
    num3 += 1

print type(range(3, 100, 3))

