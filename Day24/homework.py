#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/29 17:53
@author: 柴顺进
@file: homework.py 
@software:rongda
@note: 
"""  
'''
翻译成现代汉语：
在笼子里有鸡（雉）和兔子在一起。
从上面数共有三十五个头，从下面数一共有九十四只脚
问一共有多少只鸡、兔子？
x+y=35
2x+4y=94
'''
import numpy as np

a = np.mat("1 1;2 4")
b = np.array([35, 94])
result = np.linalg.solve(a,b)
print(result)