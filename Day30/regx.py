#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 16:18
@author: 柴顺进
@file: regx.py 
@software:rongda
@note: 
"""
import re
strs = '1042503人评价'
reg = re.compile('(\d*)')
print(re.findall(reg,strs))

