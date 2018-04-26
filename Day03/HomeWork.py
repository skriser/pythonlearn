#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 14:52
@author: 柴顺进
@file: HomeWork.py 
@software:rongda
@note: 第二章基础练习
"""
import  json
# info = {}
# info['zhangsan'] = {'age':20,'sex':'男','habbit':'play ball'}
# info['lisi'] = {'age':25,'sex':'male','habbit':'learn'}
# print info
# info['xiaohong'] = {'age':18,'sex':'female','habbit':'travel'}
# print info
# info['lisi']['age'] = 40
# print info['lisi']
# del info['lisi']
# print info

list1 = ['zhangsan', 20, 'male', 'play ball']
list2 = ['lisi', 25, 'male','learn']
list3 = ['xiaohong', 18, 'female', 'travel']
lista = [list1, list2, list3]
info = {}
info_value = {}

for i in range(3):
    info[lista[i][0]] = {'age': lista[i][1], 'sex': lista[i][2], 'hobby': lista[i][3]}
print info