#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 11:43
@author: 柴顺进
@file: 06demofor.py 
@software:rongda
@note: 字典推导式，for循环
"""  
# city = {'张三':['a','b','c'],'李四':[1,2,3,4,5]}
#
# name = raw_input("请输入姓名：")
#
# for name in city.keys():
#     for c in city[name]:
#         print name, c

a = [1,324,234,5,34,23,3346]

print sum(a)/len(a)

for i in range(0,10):
    for j in range(1,i):
        print i, j,
        # print j*i,
    print
