#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/28 16:40
@author: 柴顺进
@file: 日期的格式化.py 
@software:rongda
@note: 
"""  
from datetime import datetime

dateStr = "2018-5-28"
newDate = datetime.strptime(dateStr, "%Y-%m-%d")
print(newDate)
weekday = newDate.date().weekday()
print("{}是星期{}".format(dateStr,weekday+1))