#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/24 9:25
@author: 柴顺进
@file: 拖拽页面.py 
@software:rongda
@note: 
"""
import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
url = 'https://www.tmall.com/'
driver.get(url)
driver.maximize_window()
time.sleep(3)
# 通过document.body.scrollHeight获取屏幕高度，然后再通过script命令执行滚动命令
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)
# scrollTo 这个是从起始位到指定位置
driver.execute_script("window.scrollTo(document.body.scrollHeight, document.body.scrollHeight+400);")
# scrollBy 这个是每次走多少
driver.execute_script("window.scrollTo(0, document.body.scrollHeight/2);")
#  ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()