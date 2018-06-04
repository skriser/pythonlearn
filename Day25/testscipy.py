#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/30 16:13
@author: 柴顺进
@file: testscipy.py 
@software:rongda
@note: 
"""  
from scipy import stats

norm = stats.norm.rvs(size=100)
kurt,pvalue = stats.kurtosistest(norm)
print(kurt,pvalue)