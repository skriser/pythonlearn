#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 9:28
@author: 柴顺进
@file: 00sum.py 
@software:rongda
@note: 对于一个函数的求和
"""  


def convert(args):
    if str(args).strip().isdigit():
        return int(args)
    else:
        return 0


def sumData(num1, num2, *args, **kwargs):
    sum1 = convert(num1)+convert(num2)
    for i in args:
        sum1 = convert(i) + sum1
    for j in kwargs.values():
        sum1 = convert(j) + sum1
    return sum1

a = sumData('1',2,3,'4',5,'hello',a1=2,b1=3)
print a

# print 'hello0'.isdigit()
# print '40'.isdigit()
