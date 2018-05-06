#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/06 13:23
@author: 柴顺进
@file: 04DecoratorLogin.py 
@software:rongda
@note: 使用装饰器判断输入的账号密码是否存在，若存在，则显示“XX欢迎登陆”。
"""  


def decoLogin(fun):
    def wrapper(user, password):
        print '请输入用户密码'
        if fun(user, password):
            print '欢迎登陆'
    return wrapper


@decoLogin
def judgeUser(name, password):
    if name == 'jack' and password == '123456':
        return True
    else:
        return False


judgeUser(raw_input("请输入用户名:"), raw_input("请输入密码："))