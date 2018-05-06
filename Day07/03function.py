#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 11:42
@author: 柴顺进
@file: 03function.py 
@software:rongda
@note: 参数的值传递
"""  


a = '1234556'


def print_me(a):
    # 内部变量不会对外部变量进行改变
    a = 234
    print a


print_me(1)
print a
print_me(a)
print a

