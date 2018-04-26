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
