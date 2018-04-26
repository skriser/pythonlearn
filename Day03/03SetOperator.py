#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 11:27
@author:chaishunjin 
@file: 03SetOperator.py 
@software:rongda
@note: 集合的操作
"""
# 集合操作：
# 比较：
se = {11, 22, 33}
be = {22, 55}
temp1 = se.difference(be) # 找出se中存在，be中不存在的数据
print temp1
print se
temp2 = se.difference_update(be) #找到se中存在，be中不存在的集合，覆盖掉se
print temp2
print se
print '--------------------------------- 删除-----------------------------------------------'
# 删除： discard() ,remove(),pop()
# discard() 移除不存在元素不会报错； remove() 移除不存在元素会报错；pop()移除末尾元素并返回
set3 = set({31, 32, 33})
set3.discard(11)
set3.discard(44)
set4 = set({41, 42, 43})
set4.remove(41)
set4.remove(44) # 移除不存在会报错
set5 = set({51, 52, 53})
temp3 = set5.pop()
print temp3
print set5

tem1 = se.intersection(be) # 取交集
se.intersection_update(be) # 取交集并更新自己
# t
se.isdisjoint(be) # 是否存在交集
se.issubset(be) # 是不是子集
se.issuperset(be) # 是不是父集
se.symmetric_difference_update(be) # 合并不同项
se.update(be) # 合并原值，覆盖


