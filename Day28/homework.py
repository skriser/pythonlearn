#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 18:59
@author: 柴顺进
@file: homework.py 
@software:rongda
@note: 
"""
import re
'''
1. 网上查询正则，明白其规则。尝试写出符合正则的 字符串，能写几个就都懂了
2. 尝试写邮箱，电话的正则表达式
'''

# *********@qq.com.
reg = re.compile('^[0-9a-zA-Z_]{1,20}@[0-9A-Za-z]{1,10}\.[a-z]{3}$')
res = re.search(reg,'12324s_0f@qq.com')
print(res)
# print(res.group())
re.match()