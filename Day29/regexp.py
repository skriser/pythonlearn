#!usr/bin/env python
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/05 10:37
@author: 柴顺进
@file: regexp.py 
@software:rongda
@note: 
"""  
import re

# 贪婪模式
reg = re.compile('a.*?b')
print re.findall(reg, 'aabab')