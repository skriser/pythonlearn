#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 2018/5/4 9:44
@author: 柴顺进
@file: 09test.py 
@software:rongda
@note: 定义一个函数，输入不定长度数字，返回所有位的和
"""  
# 复数 5+2j

def sumonenum(number1):
    count = 0
    for i in str(number1):
        if i != '.' and i != '-':
            count += int(i)
    return count


print sumonenum(-1233.44)

print 4*365