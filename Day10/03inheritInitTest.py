#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 14:03
@author: 柴顺进
@file: 03inheritInitTest.py 
@software:rongda
@note: 关于继承中参数的问题
"""
# class First(object):
#     num = 1
#
# class Second(First):
#     num = 2
#
# two = Second()
# two.num = 3
# print two.num


class One(object):
    def printMe(self):
        print 11111


class Two(One):
    def printMe(self):
        print 222222


xm = Two()
xm.printMe()

One.printMe(xm) # 方法名加上子类的对象
