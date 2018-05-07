#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/04 2018/5/4 10:47
@author: 柴顺进
@file: 01lambda.py 
@software:rongda
@note: 匿名函数
"""  
c = lambda x:[i for i in x if i%2 == 0 ] # 生成器，就相当于定义了一个函数c

print c([1,2,3,4,5])


def cc(x):
    list1 = []
    for i in x:
        if i % 2 == 0:
            list1.append(i)
    return list1


print cc
