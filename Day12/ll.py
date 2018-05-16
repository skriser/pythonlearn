#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/10 10:26
@author: 柴顺进
@file: ll.py 
@software:rongda
@note: 
"""  
from Day12.savexcel import SaveExcelData

data = list(range(20))
newdata = []
for i in range(4):
    newdata.append(data[5*i:5*(i+1)])

new1 = SaveExcelData(newdata, 'newdata', 'newdata.xlsx')
new1.saveData()
