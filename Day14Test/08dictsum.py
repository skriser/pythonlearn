#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 10:29
@author: 柴顺进
@file: 08dictsum.py 
@software:rongda
@note: 
"""  
dict1 = {'a': 1, 'b': 2, 'c': '3', 'd': 'hello'}
dict2 = {'a': 2, 'b': '2', 'c': 'she', 'e': '10', 'f': 4}


def sumDict(dict1, dict2):
    if len(dict1) < len(dict2):
        dict1,dict2 = dict2, dict1
    dict3 = {}
    for i in dict1.keys():
        for j in dict2.keys():
            if i == j:
                if type(dict1[i]) == type(dict2[j]):
                    dict3[i] = dict1[i]+dict2[j]
                else:
                    dict3[i] = str(dict1[i]) + str(dict2[j])
                break
        else:
            dict3[i] = dict1[i]
            dict3[j] = dict2[j]
    return dict3


print(sumDict(dict1,dict2))