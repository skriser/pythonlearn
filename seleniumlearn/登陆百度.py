#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/24 9:48
@author: 柴顺进
@file: 登陆百度.py 
@software:rongda
@note: 
"""
import time
from selenium import webdriver


class LoginBaidu(object):

    def loginBaiduByIdAndClass(self):
        driver = webdriver.Chrome()
        url = 'https://www.baidu.com'
        driver.get(url)
        login = driver.find_element_by_id('u1').find_elements_by_class_name('lb')[0]
        login.click()
        time.sleep(2)
        # 找出用户名登陆
        usernameLogin = driver.find_element_by_id('TANGRAM__PSP_10__footerULoginBtn')
        usernameLogin.click()
        username = driver.find_element_by_id('TANGRAM__PSP_10__userName')
        username.send_keys('ckriser')
        password = driver.find_element_by_id('TANGRAM__PSP_10__password')
        password.send_keys('xiao136147158')
        time.sleep(3)
        submit = driver.find_element_by_id('TANGRAM__PSP_10__submit')
        submit.click()
        time.sleep(30)

    def loginBaiduByCss(self):
        driver = webdriver.Chrome()
        url = 'https://www.baidu.com'
        driver.get(url)
        login = driver.find_element_by_css_selector('div[id=u1] a[class=lb]')
        login.click()
        time.sleep(2)
        usernameLogin = driver.find_element_by_css_selector('p.tang-pass-footerBarULogin')
        usernameLogin.click()
        username = driver.find_element_by_css_selector('input.pass-text-input-userName')
        username.send_keys('ckriser')
        password = driver.find_element_by_css_selector('input.pass-text-input-password')
        password.send_keys('xiao136147158')
        time.sleep(3)
        submit = driver.find_element_by_css_selector('input.pass-button-submit')
        submit.click()
        time.sleep(30)



logina = LoginBaidu()

# logina.loginBaiduByIdAndClass()
logina.loginBaiduByCss()