#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 11:13
@author:Charles
@file: 02Set.py 
@software:rongda
@note: 集合的基础操作
"""  

# 创建集合
# 1.字符串变为集合
set1 = set('hello')
print set1
print type(set1)
# 2.列表变为集合
list1 = [1, 2, 3, 4]
set2 = set(list1)
print set2
# 3.字典变为集合 ;set3里面变成了他的key值
dict1 = {'n1': 1, 'n2': '2', 'n3': [3, 4]}
set3 = set(dict1)
print set3
print type(set3)
# 4.直接写
set4 = {'k1', 'k2', 'k3'}
print set4








