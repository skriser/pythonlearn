#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/06 15:23
@author: 柴顺进
@file: douban_film.py 
@software:rongda
@note: 
"""
import re
import xlwt
import chardet
import requests
from bs4 import BeautifulSoup

# index = 0 获取某一页的内容
def getHtml(pageNumber):
    tag_all = []
    for i in range(pageNumber):
        url = 'https://movie.douban.com/top250/?start={}'.format(i*25)
        r = requests.get(url)
        code = chardet.detect(r.content)['encoding']
        r = r.content.decode(code)
        tag_all.append(r)
    return tag_all


def dataList(html_list):
    data_list = []
    for html in html_list:
        soup = BeautifulSoup(html,'html.parser')
        # 获取想要的东西
        parent_content = soup.find('div', attrs={'id': 'content'})
        li_list = parent_content.find_all('li')
        for each in li_list:
            # 电影名称
            movieName = each.find('div',{'class':'hd'}).find('span',{'class':'title'}).string
            # 上映时间
            releaseTime = each.find('div',{'class':'bd'}).find('p').getText()
            reg = re.compile('.*(\d{4}).*')
            releaseTime = str(re.findall(reg,releaseTime)[0])
            # 评分
            ratingNum = each.find('div', {'class': 'star'}).find('span', {'class': 'rating_num'}).string
            # 评论人数
            reviewNum = each.find('div', {'class': 'star'}).find_all('span')[3].getText()
            reg = re.compile('(\d*)')
            reviewNum = str(re.findall(reg, reviewNum)[0])
            # 简评
            if each.find('div',{'class':'bd'}).find('p',{'class': 'quote'}):
                comment = each.find('div', {'class': 'bd'}).find('p', {'class': 'quote'}).find('span',{'class':'inq'}).getText()
            else:
                comment = ''
            data_list.append([movieName, releaseTime, ratingNum, reviewNum, comment])
    return data_list


def saveXLS(data_list):
    wbk = xlwt.Workbook()
    wst = wbk.add_sheet("豆瓣电影top250")
    for i, row in enumerate(data_list):
        for j, value in enumerate(row):
            wst.write(i, j, value)
    wbk.save("豆瓣电影top250.xls")


def main(pageNumber):
    tag_list = getHtml(pageNumber)
    data_list = dataList(tag_list)
    print(data_list)
    saveXLS(data_list)

main(10)