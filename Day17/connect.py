#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 13:45
@author: 柴顺进
@file: connect.py 
@software:rongda
@note: pymysql connect
"""  
import pymysql


def getConnect(host,user,password,db,charset):
    connect = pymysql.connect(host=host, user=user, password=password, db=db, charset=charset)
    return connect


if __name__ =='__main__':
    print('conn.py文件自身被运行了')

