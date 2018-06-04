#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/31 14:44
@author: 柴顺进
@file: homework-reaseaonactiion.py 
@software:rongda
@note: 
"""
'''
获取昨日排行第一的电影信息包含（名称、累计票房及上映天数），
显示该电影自放映到昨日的所有累计票房线性趋势。
提示： ts.day_boxoffice(‘ 日期 ’) 方法获取单日电影票房数据
0       33         1       392          -80     1       14        超时空同居   
'''
import datetime
import tushare as ts
from matplotlib import pyplot as plt
boxOffice = []
movieDay = []
# ['2018-05-22', '2018-05-23', '2018-05-24', '2018-05-25', '2018-05-26', '2018-05-27', '2018-05-28', '2018-05-29', '2018-05-30']

begin = datetime.date(2018,5,22)
end = datetime.date(2018,5,30)
d = begin
delta = datetime.timedelta(days=1)
while d <= end:
    movieDay.append(d.strftime("%Y-%m-%d"))
    d += delta
print(movieDay)
for day in movieDay:
    data = ts.day_boxoffice(day)
    print(data[:1])
    boxOffice.append(data[:1].SumBoxOffice)

print(boxOffice)
plt.plot(movieDay,boxOffice,'o',movieDay,boxOffice,'-')
plt.show()


def data2str(n):
    today = datetime.today()
    delta = datetime.timedelta(days=n)
    start = today - delta
    return start.strftime("%Y-%m-%d")