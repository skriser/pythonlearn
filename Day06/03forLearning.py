#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 9:41
@author: 柴顺进
@file: 03forLearning.py 
@software:rongda
@note: 练习
"""  

# 与7相关的数：7的倍数,取模为零，开头为7 取整为7  //10 == 7 ，结尾为7：余数是7 ：%10 == 7，
# for i in range(1, 100):
#     if i % 7 == 0 or i % 10 == 7 or i // 10 == 7:
#         print i,

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['a', 'b', 'c']
c = []
for i in range(len(list1)):
    for j in range(len(list2)):

        if list1[i] == list2[j]:
            c.append(list1[i])
print c

print [x**2 for x in range(1,11)]


