#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/07 14:46
@author: 柴顺进
@file: 04string.py 
@software:rongda
@note: 常用字符串操作方法
"""
# 首字符大写
print 'hello'.capitalize()

# string.count(str, beg=0, end=len(string))
s1 = 'my name is jack, his name is haha'
print s1.count('is',0,len(s1))

# endswith()检查以什么为结尾
s1.endswith('haha')

# ecpandtabs() 将table符号转为空

# find()
# print s1.find('haha',0,len(s1))
# if s1.find('haha',0,len(s1)) != -1:
#     print 'you'
#
# # format
#
# # index()
# print s1.index('has', 0, len(s1))
#
s1.isalnum()

# islower() 判断是不是小写
print s1.islower()
s6 = 'hello'
print '--'.join('hello')

# replace() 替换
s7 = 'his name is Jack,ss'
print s7.replace('is', 'was',1)

#split()
s9 = '12 34 56 78'
print s9.split(' ', 1)
print s9.replace(' ', '')
print s9.split()
print ''.join(s9.split())
