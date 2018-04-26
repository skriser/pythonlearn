#!usr/bin/env python  
# -*- coding:utf-8 *-
""" 
@time: 2018/04/26 2018/4/26 15:42
@author: 柴顺进
@file: 06if.py 
@software:rongda
@note: 控制语句 if 在Python中没有switch语句
"""  
money = int(raw_input("今年我有压岁钱："))
if money > 5000:
    print '买买买'
elif money > 4000:
    print '买个中等的'
elif money > 3000:
    print '买个 低 的'
else:
    print '要不起'
