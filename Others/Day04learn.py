#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/27 2018/4/27 11:10
@author: 柴顺进
@file: Day04learn.py 
@software:rongda
@note: 回顾小知识点
"""
# #a ,b 值互换
a = 10
b = 20
a, b = b, a
print a, b

# 2.判断用户输入是否是一个数
c = raw_input(":")
if c.strip().isdigit():
    print a
else:
    print "不是一个数"

# 取最大的值，谁大取谁
aa = 2
bb = 3
cc = aa if aa > bb else bb
print cc


