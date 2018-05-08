#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/08 13:19
@author: 柴顺进
@file: 03dateTime.py 
@software:rongda
@note: 日期和时间的函数
"""  
import time
import calendar
Now = time.time()
print(Now)

# time.localtime()时间元组，由python元组组成的数值
# time.struct_time(tm_year=2018, tm_mon=5, tm_mday=8, tm_hour=13, tm_min=24, tm_sec=31, tm_wday=1, tm_yday=128, tm_isdst=0)
#
Now = time.localtime()
print(Now)
# 格式输出
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
# 格式化成2016-03-20 11:45:39形式
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

# cal
cal = calendar.month(2018, 5)
print(cal)
print(calendar)