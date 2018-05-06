#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 14:09
@author: 柴顺进
@file: 必备参数.py 
@software:rongda
@note: 
"""  


def print_me(str):
    print str

print_me('sd')


def printInfo(name, age=35):
    print name, age
    return

printInfo('jack',20)
printInfo('Miki')


# 不定长参数：
def funC(x, y, z, *args, **kwargs):
    print x, y, z
    print args
    print kwargs


funC(1, 2, 3, 4, 5, 6, 7, a='hello', b='world')
