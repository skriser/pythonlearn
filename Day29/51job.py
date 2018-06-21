#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/05 11:31
@author: 柴顺进
@file: 51job.py 
@software:rongda
@note: 爬虫51job文件
"""  
import re
from getHtml import getHtml
import chardet
import xlwt
# def getHtml(url):
#     User_Agent = []
#     Proxies = []
#     req = urllib2.Request(url)
#     res = urllib2.urlopen(req)
#     return res.read()

# 1.获取51job职位搜索信息
url = 'https://search.51job.com/list/020000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='
html = getHtml(url)
print(chardet.detect(html)) # 获取网页返回的网页编码
# 获取网页对象的编码进行转码
code = chardet.detect(html)['encoding']
html = html.decode(code).encode('utf-8')
# print html

# 2.匹配正则表达式
'''
<span>.*<a target="_blank" title="(.*?)" href=.*>(.*?)</a>.*</span>.*</p>
'''
# 怎么使用正则匹配呢
pattern = re.compile(r'<p class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',re.S) # re.S 是匹配多行的意思，因为网页是由多行组成
result = re.findall(pattern,html)

# 存到xls

workbook1 = xlwt.Workbook(encoding='utf-8')
# 创建工作表
sheet = workbook1.add_sheet('51job-python-职位信息')
#
col = ('1','2','3','4')
for i in range(len(col)):
    sheet.write(0,i,col[i])
for i in range(len(result)):
    for j in range(len(result[i])):
        sheet.write(i+1,j, result[i][j])

workbook1.save('51jobas.xls')