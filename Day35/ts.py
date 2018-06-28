#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/21 9:30
@author: 柴顺进
@file: ts.py 
@software:rongda
@note: 
"""  
from pandas import Series,DataFrame
import pandas as pd

series = Series([1,-999,2,-999,-1000,3])
series.replace([-999,-1000],'sd')

cats = pd.cut(age,bins)
DataFrame.applymap()
str.capitalize()
DataFrame.duplicated()
DataFrame.drop_duplicates()

pd.value_counts