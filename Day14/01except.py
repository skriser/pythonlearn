#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 13:50
@author: 柴顺进
@file: 01except.py
@software:rongda
@note: 
"""  
# try:
#     aa
# except:
#     print('有错误')
# print(23)


# 语法错误的话就无法执行到自定义的异常处理，因为语法错误无法编译通过
try:
    if('aa'+1):
        dfg
except NameError:
    print('Name有错误')
except TypeError:
    print('类型错误')
except:
    print('其他错误都走这个')
else:
    print('无错误的时候执行这个')