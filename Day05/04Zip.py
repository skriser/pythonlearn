#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/04/28 2018/4/28 13:28
@author: 柴顺进
@file: 04Zip.py 
@software:rongda
@note: zip()函数的基本使用
"""  

# list1 = ['hello', 'world', 'yes']
list1 = ['hello', 'world']
list2 = [1, 2, 3]
list3 = ['boy', 'girl', 'boy']
list4 = {'zhangsan', 'lisi', 'wangwu'}
# print zip(list1, list2)
# print zip(list2, list1)

d = []
# for x, y in zip(list1, list2):
#     d.append(x + str(y))
# print d

for x, y, z in zip(list1, list2, list3):
    d.append(x+'-'+str(y)+'-'+z)
print d

dict1 = {}