#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/01 15:49
@author: 柴顺进
@file: test3.py 
@software:rongda
@note: 
"""
import datetime
import tushare as ts
import numpy as np
from scipy import signal
from matplotlib import pyplot as plt
from matplotlib.font_manager import FontProperties

'''
3、请使用tushare模块提供的api并结合numpy、scipy等模块，
获取前一天电影排行数据中上映天数大于7中日平均票价最高的电影，
分析该电影近一个星期的票房及电影票价的走势，
要求分别绘制出票房走势和平均票价走势
'''
today = datetime.date.today()
delta = datetime.timedelta(days=1)
yesterday = (today -delta).strftime("%Y-%m-%d")
data = ts.day_boxoffice(yesterday)
movieDay,movieName,moviePrice = data.MovieDay,data.MovieName,data.AvgPrice
#获取需要分析的电影的名称
targetMovieName = None
tmpMoviePrice = 0
#通过循环，找到上映天数大于7天并且平均票价最高的电影
for name,day,price in zip(movieName,movieDay,moviePrice):
    if int(day)>7:
        if tmpMoviePrice < int(price):
            tmpMoviePrice = int(price)
            targetMovieName = name

def date2num(n):
    today = datetime.date.today()
    delta = datetime.timedelta(days=n)
    start = today - delta
    return start.strftime("%Y-%m-%d")
targetBoxOffice = []
#存放近10天日期的字符串
dates = []

for i in range(0,7):
    start = date2num(i+1)
    #将日期添加到日期列表中
    dates.append(start)
    #循环获取7天电影票房的排行信息
    day = ts.day_boxoffice(start)
    dayMovieName = day.MovieName
    dayBoxOffice = day.BoxOffice
    for name,boxOffice in zip(dayMovieName,dayBoxOffice):
        #判断每日票房排行中的电影名称是否为需要分析的电影
        if name == targetMovieName:
            targetBoxOffice.append(boxOffice)
            # print(name,boxOffice)

targetBoxOffice = np.array(targetBoxOffice,dtype=np.float64)
dates = np.array(dates)

newDates = dates[::-1]
newBoxOffice = targetBoxOffice[::-1]
y = signal.detrend(newBoxOffice)
plt.figure(num=1, figsize=(10, 8))
#为图加上标题
font_set = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=15)
title = "《"+targetMovieName+"》近十天票房走势"
plt.title(title,size=25,fontproperties=font_set)
plt.plot(newDates,newBoxOffice,"-",newDates,newBoxOffice-y,"-")
plt.show()
