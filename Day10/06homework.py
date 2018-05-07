#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 17:48
@author: 柴顺进
@file: 06homework.py 
@software:rongda
@note: 第十天练习
"""
# 3.冰淇淋小店：冰其淋小店是一种特殊的餐馆。
# 编写一个名为IceCreamStand的类，让 它继承你为完成练习1而编写的Restaurant类。
# 添加一个名为flavors的属性,用于存储一个 由各种口味的冰淇淋组成的列表。
# 编写一个显示这些冰淇淋的方法。
# 创建一 IceCreamStand实例,并调用这个方法。


class Restaurant(object):

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print '餐馆名称：', self.restaurant_name
        print '主要烹饪食物：',self.cuisine_type

    def open_restaurant(self):
        print self.restaurant_name, '正在营业中'


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super(IceCreamStand,self).__init__(restaurant_name, cuisine_type)
        self.flavors = ['dd', 'huw', 'nsadfice']

    def show_flavors(self):
        for n in self.flavors:
            print('my favorate taste is ' + n)


ss = IceCreamStand('cai', 'ICE')
ss.show_flavors()


