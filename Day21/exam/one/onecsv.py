#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/24 9:08
@author: 柴顺进
@file: onecsv.py 
@software:rongda
@note: 
"""
import csv

list1 = []
with open("data.csv",) as file:
    reads = csv.reader(file)
    for i in reads:
        list1.append(i)
        print(i)
    file.close()
with open("data1.csv", "w",newline="") as file1:
    writes = csv.writer(file1)
    list1.append(["jack", "104"])
    for row in list1:
        writes.writerow(row)
    file1.close()


