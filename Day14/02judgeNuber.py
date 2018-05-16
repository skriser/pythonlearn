#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/13 14:27
@author: 柴顺进
@file: 02judgeNuber.py 
@software:rongda
@note: 
"""
# 输入两个数，判断除数是零的时候提示异常
# while 1:
#     begin = input('是否开始Y/N:')
#     if begin.lower() == 'y':
#         num1 = input('请输入Num1:')
#         num2 = input('请输入num2:')
#         try:
#             print(int(num1)/int(num2))
#         except ZeroDivisionError:
#             print('你干啥让除数为零？')
#         else:
#             pass
#     else:
#         break

# 几种异常在一起的时候
# try:
#     print(aa)
#     # 几种异常放到一起合并处理，使用元组进行
# except (TypeError,NameError):
#     print('这几种错误')

# try -- finally
try:
    print('aa'+1)
except NameError:
    print('nameError')
except TypeError:
    print('TypeError')
else:
    print('正常执行')
finally:
    print('不管前面如果，我都要最后执行')
