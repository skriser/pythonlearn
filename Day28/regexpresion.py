#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/04 15:34
@author: 柴顺进
@file: regexpresion.py 
@software:rongda
@note: Regular Expression
"""  
import re

# 正则表达式
pattern = re.compile('hello',re.I)


res1 = re.match(pattern,'hello')
res2 = re.match(pattern,'hello CQC')
res3 = re.match(pattern,'helo')
res4 = re.match(pattern,'Hello')
res5 = re.search(pattern,'aaa Hello')
# print res1
# print res2
# print res3
# print res4
# print res5

# 其他的匹配方式
# reg = re.compile('^he') # 开头
# reg1 = re.compile('jack$') # ^ d
# print re.search(reg, 'he is jack...')

# 计数 * 匹配
# reg = re.compile(r'\bis{1}\b')
# print re.search(reg, 'his name is haha is haha')

#
reg = re.compile('\d{4}')
print re.search(reg,'d3d3d3s3d3f4faw3sfaw3')