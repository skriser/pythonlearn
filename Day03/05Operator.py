#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 13:36
@author: 柴顺进
@file: 05Operator.py 
@software:rongda
@note: 运算符操作
"""
a = 18
b = 10
if a == b:
    print "yes"
else:
    print "no"

# 赋值运算符
a = 10
b = 5
c = 0
c+=a # c = c+a
b-=a # b = b-a
a**=b # a =a**b

# b 二进制， o 八进制，x: 十六进制
# bin() ,oct(),hex()
# print bin(200)
# print oct(200)
# print hex(200)
# print "  in  %o"%20

a = 1
b = 1
print a is b
list1 = [1, 2, 3]
list2 = list1[:]
print list1 is list2
print list1 == list2 # 判断值
print list1[0] is list2[0]
print id(list1[0])
print id(list2[0])
print id(1)
print id(a)
