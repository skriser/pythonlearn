#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 13:23
@author: 柴顺进
@file: 51job4bs4.py 
@software:rongda
@note: 
"""
import chardet
import requests
from bs4 import BeautifulSoup
url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,Python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='


r = requests.get(url)
code = chardet.detect(r.content)['encoding']
r.encoding = code
soup = BeautifulSoup(r.text, 'html.parser')
parentDiv = soup.find('div', {'id':'resultList'})
p1 = parentDiv.find_all('div', {'class': 'el'})
p1.pop(0)
List_All = []
for enum in p1:
    data1 = enum.find('p').find('a').text.strip()
    data2 = enum.find('span', {'class':'t2'}).a.text
    data3 = enum.find('span', {'class':'t3'}).text
    data4 = enum.find('span', {'class': 't4'}).text
    data5 = enum.find('span', {'class': 't5'}).text
    List_All.append([data1, data2, data3, data4, data5])

print(List_All)

import xlwt
wbk = xlwt.Workbook()
wst = wbk.add_sheet("python")
for i, row in enumerate(List_All):
    for j, value in enumerate(row):
        wst.write(i, j, value)
wbk.save("python.xls")

