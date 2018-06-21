#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 11:44
@author: 柴顺进
@file: getimagesrc.py 
@software:rongda
@note: 
"""
import chardet
import requests
from bs4 import BeautifulSoup

r = requests.get('http://images.baidu.com')
code = chardet.detect(r.content)['encoding']
r.encoding = code
soup = BeautifulSoup(r.text,'html.parser')
imgList = soup.find_all('img')
for i in imgList:
    print(i)