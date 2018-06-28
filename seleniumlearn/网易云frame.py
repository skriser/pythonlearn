#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/24 16:39
@author: 柴顺进
@file: 网易云frame.py 
@software:rongda
@note: 
"""  
from selenium import webdriver

driver = webdriver.Chrome()
url = 'https://music.163.com/#/discover/toplist'
driver.get(url)
# 11.切换进入到frame中 1.根据id直接去切换
driver.switch_to.frame('g_iframe')  # 这个存在个问题可能找不到
# print(driver.find_elements_by_tag_name('tr'))
# print('###################################################')
# # 22.切换进入到frame中 2.根据id先找到这个tag 再去切换 # 直接切换失败的可以直接这样搞
# myframe = driver.find_element_by_id('g_iframe')
# driver.switch_to.frame(myframe)
# trs = driver.find_elements_by_tag_name('tr')
# for i in trs:

parent = driver.find_element_by_id('song-list-pre-cache')

table = parent.find_elements_by_tag_name('table')[0]
tbody = table.find_elements_by_tag_name('tbody')[0]
trs = tbody.find_elements_by_tag_name('tr')

for each in trs:
    # print(each.find_elements_by_tag_name('td')[0].text)
    print(each.find_elements_by_tag_name('td')[3].find_elements_by_tag_name('div')[0].get_attribute('title'))


