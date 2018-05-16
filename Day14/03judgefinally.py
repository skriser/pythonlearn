#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 15:20
@author: 柴顺进
@file: 03judgefinally.py 
@software:rongda
@note: 
"""  
# 捕捉并把捕捉到的异常打印出来

def qiushang():
    x = 1/0
    x += 2


try:
    qiushang()
except Exception as tip:
    print(tip)
