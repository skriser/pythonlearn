#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 10:33
@author: 柴顺进
@file: beautiful.py 
@software:rongda
@note: 
"""  
from bs4 import BeautifulSoup

html = """  
<html><head><title>The Dormouse's story</title></head>  
<body>  
<p class="title" name="dromouse"><b>The Dormouse's story</b></p>  
<p class="story">Once upon a time there were three little sisters; and their names were  
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,  
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and  
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;  
and they lived at the bottom of a well.</p>  
<p class="story">...</p>  
"""

# 获取对象，使用python默认的解析器 parser ：解析器
soup = BeautifulSoup(html,'html.parser')
# # print(dir(soup))
# print(soup.title)
# print(soup.head)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.get_text())
# # 通过上下级关系获取对象 parent
# print(soup.title.parent)
# 通过上下级关系获取 child children
# print(soup.p) # 有很多p标签，默认匹配第一个
# print(soup.p.child)
# print(soup.p.children)
# for i,each in enumerate(soup.p.children):
#     print(i,each)
# print(soup.find('p'))
# print(soup.find_all('p'))

# a = soup.a
# print(a)
# print('a.name:', a.name)
# print('a.attrs:', a.attrs)
# print('a.text:', a.text)
# print('a.id:', a.id)
# print('a[\'id\']:', a['id'])

print(soup.find_all('a', {'id': 'link3'})) # a标签，id为link3的
print(soup.find_all('a', {'class': 'sister'})) # a标签，class为sister的

a_link3 = soup.find('a', {'id': 'link3'})
print(a_link3['href'])