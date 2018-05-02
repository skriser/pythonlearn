#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 9:25
@author: 柴顺进
@file: 02enumerate.py 
@software:rongda
@note: enumerate 使用
"""  
letter = ['a', 'b', 'c', 'd', 'e']

for i in range(len(letter)):
    print letter[i], ' is ', i+1

a = 1
for i in letter:
    print i, ' is ', a
    a += 1

# for 下标 ，值 in enumerate()
for index, value in enumerate(letter):
    print value, 'is', index
