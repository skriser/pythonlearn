#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 11:27
@author: 柴顺进
@file: 01inherit.py 
@software:rongda
@note: python中的继承:python中object是所有对象的父类
"""  


class Animal(object):

    def __init__(self, name, food):
        self.name = name
        self.food = food

    def voice(self, v):
        print self.name, '叫出了', v


class Dog(Animal):

    def __init__(self, name, food, age):
        super(Dog,self).__init__(name, food) # 继承自父类的属性
        self.age = age # 自己的属性


class Cat(Animal):

    def __init__(self, name, food, attract_num):
        super(Cat,self).__init__(name,food)
        self.attract_num = attract_num


# 布偶猫，又称“布拉多尔（Ragdoll）”，发源于美国，是一种杂交品种宠物猫。
# 是现存体型最大、体重最重的猫之一。
ragdoll = Cat('布偶', '鱼', 5)
Husky = Dog('饭团', '肉', 2)
Husky.voice('嗷呜。。')
ragdoll.voice('m喵喵。。')

