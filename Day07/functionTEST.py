#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/03 2018/5/3 13:20
@author: 柴顺进
@file: functionTEST.py 
@software:rongda
@note: 
"""  


def judeyear(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        print year, 'is runnian'


def getSqrt(num):
    print num**2, num**3


def printStar(line):
    for i in range(line+1):
        for j in range(i):
            print "*",
        print

def printStar1(line):
    for i in range(line+1):
        for j in range(i):
            print "*",
        print


printStar1(5)

# judeyear(64)
# getSqrt(2)
# printStar(4)
