#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 16:19
@author: 柴顺进
@file: day09homework01.py
@software:rongda
@note: 
"""  
# 1.餐馆：创建一个名为Restaurant的类，其方法__init__()设置两个属性： restaurant_name 和 cuisine_type(烹饪)。
# 创建一个名为 describe_restaurant() 方法和一个名为open_restaurant()方法,其中前者打印前述两项信息，而后者打
# 印一条消息,指出餐馆正在营业。 根据这个类创建一个名为restaurant的实例，分别打印其两个属性，再调用前述 两个方法。
# 根据你为完成上面的练习而编写的类创建三个实例，并对每个实例调用方法 describe_restaurant()。


class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print '餐馆名称：', self.restaurant_name
        print '主要烹饪食物：',self.cuisine_type

    def open_restaurant(self):
        print self.restaurant_name, '正在营业中'


restaurant1 = Restaurant('玫瑰', '关于花的食物')
restaurant1.describe_restaurant()
restaurant1.open_restaurant()


restaurant2 = Restaurant('小酒馆', '关于酒的食物')
restaurant3 = Restaurant('小面馆', '关于面的食物')
restaurant4 = Restaurant('小茶馆', '关于茶的食物')
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
restaurant4.describe_restaurant()
