#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 9:49
@author: 柴顺进
@file: day8homework.py 
@software:rongda
@note: 
"""  

# 3.编写函数，输入某年某月某日，判断这一天是这一年的第几天
# 2018 5 4
# 1 月31天，2月 28 天，3月 31天 ,4月30天 5月4天
# def judge_day(year, month, day):
#     day_count = 0
#     dict_day1 = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
#     for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
#         if month == i:
#             break
#         day_count += dict_day1[i]
#     if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0) and month > 2:
#         day_count += 1
#     day_count += day
#     return day_count


def sum_day(year, month, day):
    list1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    list2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year%4==0 and year%100!=0 or year%400==0:
        print "这个总共有",sum(list1[:month-1])+day,'天'
    else:
        print "这个总共有",sum(list2[:month - 1]) + day,'天'


sum_day(2301, 12, 22)

# 闭包的作用是在外部的操作a 函数的内部变量，因为调用a函数会返回一个c函数c函数是可以对a函数里面的内容进行调用的，
# 这样就可以通过访问返回的c函数进行a
# 函数进行调用了
def a():
    b = 10
    def c():
        return b
    return c

d = 20

f = a()

print(d+f())
