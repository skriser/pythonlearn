#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 14:48
@author: 柴顺进
@file: 08CreateClass03.py 
@software:rongda
@note: 
"""
# from 文件名 import 类名
# from CreateClass import Employee
from CreateClass import Employee

e1 = Employee('张三', 20000)
e1.showInfo()

print getattr(e1, "name")
print setattr(e1, 'age', 20)
print hasattr(e1, 'age')
print e1.age
print delattr(e1, 'age')
# e1.age

print Employee.__dict__ # 类的属性
print Employee.__doc__ # 类的文档
print Employee.__name__ # 类的类名
print Employee.__module__ # 类的模块
print Employee.__bases__ # 类的父类信息
