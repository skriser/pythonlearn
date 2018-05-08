#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 11:09
@author: 柴顺进
@file: 02dict.py 
@software:rongda
@note: 字典的函数使用
"""  
# str(dict)
dict1 = {'a': 1, 'b': 2, 'c': [4, 5]}
print(type(str(dict1)))

# # dict.clear() 删除字典内的所有元素
# print(dict1.clear())
# print(dict1)
# copy() 返回一个字典的浅复制
dict2 = dict1.copy()
print(id(dict1))
print(id(dict2))
list1 = [1, 2]
list2 = list1.copy()
print(id(list1))
print(id(list2))
# dict.fromkeys(seq[,val] ,重新以建和值进行分配复制出来的
dict3 = {}.fromkeys(['a', 'b'],21)
print(dict3)
dict3 = {}.fromkeys(['a', 'b'],21)
print(dict3)
# get("key") 不存在的返回None
dict3.get('a')
# items 返回可以遍历的元组组成的列表
print(dict3.items())
# update()

# pop()

# popitem()