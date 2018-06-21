#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 15:02
@author: 柴顺进
@file: beautifulsoupLearn.py 
@software:rongda
@note: 
"""
import re

from bs4 import BeautifulSoup

html = """
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p>12345</p>  
<p>123456</p>  
<p>abcde</p>
<p>abcdef</p>
<div><p>第二代P</p><div>
</body>  
"""

soup = BeautifulSoup(html, 'html.parser')
# 通过内容进行匹配
print(soup.find_all('p',text=12345))
# 使用正则匹配，限定内容进行匹配
print(soup.find_all('p', text=re.compile('\d{1}')))
print(soup.find_all('p', text=re.compile('abcde')))
print(soup.find_all('p', text=re.compile('(abcde){1}'),limit=1)) # 限定找的次数，只查找一次
# 查找层数限定
print(soup.find('body').find_all('p')) # 查找所有的
print(soup.find('body').find_all('p',recursive=False)) # Ture查找所有，False 只是查找第一层