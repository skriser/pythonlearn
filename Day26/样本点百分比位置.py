#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/31 9:57
@author: 柴顺进
@file: 样本点百分比位置.py 
@software:rongda
@note: 
"""  
from scipy import stats

normalExample = stats.norm.rvs(size=100)
# 找打位于数据95%位置的数据点
result = stats.scoreatpercentile(normalExample,95)
print("数据样本的95%的位置的数据点：",result)

percet = stats.percentileofscore(normalExample,0.8)
print("0.8在数据样本中的位置",percet)