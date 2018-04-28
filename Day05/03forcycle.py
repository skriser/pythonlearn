#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/04/28 2018/4/28 11:17
@author: 柴顺进
@file: 03forcycle.py 
@software:rongda
@note: for循环基础学习
"""  

# # 遍历字符串
# a = 'python'
# print a[0:5]
# # 使用while遍历a
# i = 0
# while i < len(a):
#     print a[i],
#     i += 1
# k = 0
# while k in range(len(a)):
#     print a[k],
#     k += 1
#
# # 使用for循环遍历a
# for i in a:
#     print i,
#
# for i in range(len(a)):
#     print a[i],

# num = [1]
# word = ["周一", "周二", "周三"]
# haxa = ['heiehi', 'haha', 'oo', 'sf']
# # for i in range(len(num)):
# #     print num[i], "is ", word[i]
# for a, b, c in zip(word, num, haxa):
#     print a, "is ", b, "zuihou", c

a = [5, 6, 7, 8, 9]
b = [5, 4, 3, 2, 1]
c = []
d = []
# for i in range(len(a)):
#     c.append(a[i]+b[i])
# print c
for x, y in zip(a, b):
    d.append(x+y)
print d

print zip(a,b)

