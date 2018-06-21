#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/12 13:40
@author: 柴顺进
@file: sympy学习导数.py 
@software:rongda
@note: 
"""  
from sympy import Symbol
from sympy import limit
from sympy import diff
from sympy import *
x = Symbol('x')
f = (x+1)**2+1
# 求x-->2 时f = (x+1)**2+1 函数的极限
print(limit(f,x,2))
# 求导数
print(diff(x**3 +2*x,x))
print(diff(4*x))
# 求不定积分
f = 3*x**2 +1
print(integrate(f,x))
