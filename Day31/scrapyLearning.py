#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/08 9:19
@author: 柴顺进
@file: scrapyLearning.py 
@software:rongda
@note: 
"""

#encoding:UTF-8
def yield_test(n):
    for i in range(n):
        yield call(i)
        print("i=",i)
    #做一些其它的事情
    print("do something.")
    print("end.")

def call(i):
    return i*2

#使用for循环
for i in yield_test(5):
    print(i,"通过迭代yield")

yield_test(5)