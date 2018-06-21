#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/07 19:19
@author: 柴顺进
@file: homeworkimg.py 
@software:rongda
@note: 
"""  
import requests
from bs4 import BeautifulSoup
import os
import chardet
#获取html
r = requests.get('https://unsplash.com/search/photos/nature')
#用BS解析html
code = chardet.detect(r.content)['encoding']
r.encoding = code
soup = BeautifulSoup(r.text, 'html.parser')
img_box = soup.find('div', {'id': 'gridMulti'})
all_image = img_box.find_all('div', {'class': '_1pn7R'})
#逐个将图片保存到本地
for index, each in enumerate(all_image):
    img = each.find('img', attrs={'itemprop':'thumbnailUrl'})
    img_real = img['src']
    img_content = requests.get(img_real).content
    file_name = str(index) + '.jpg'
    with open(os.getcwd() + '/image/' + file_name, 'wb') as wf:
        wf.write(img_content)