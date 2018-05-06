#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 13:47
@author: 柴顺进
@file: 06CreateClass.py 
@software:rongda
@note: python 2.2之前是用class来创建类
"""


# 新建一个雷
class Car:
    doors = 4 # 这个里面是类里面自动生成

    # 固定写法 init函数，规定这个类有哪些基本属性
    def __init__(self, name, color): # 这两个参数是用来使用函数初始化时候使用的
        self.name = name
        self.color = color

    def showinfo(self):
        print 'This car is called %s,%s' % (self.name, self.color)


car1 = Car('BMW', 'Black')
car2 = Car('QQ飞车', 'Yellow')
# car3 = Car()

car1.showinfo()
car2.showinfo()
