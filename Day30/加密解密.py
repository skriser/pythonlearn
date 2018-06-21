#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 10:20
@author: 柴顺进
@file: 加密解密.py 
@software:rongda
@note: 
"""  

from urllib import parse
st2 = '人工智能'
print(parse.quote(st2))
print(parse.unquote(parse.quote(st2)))