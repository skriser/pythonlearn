#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 15:30
@author: 柴顺进
@file: mysqlmodify.py 
@software:rongda
@note: 
"""  
from Day17.connect import getConnect


def modifyData(data):
    conn = getConnect("localhost", "root", "root", "shop", "utf8")
    sql = "update commoditytype set ct_name = '%s' where ct_id = '%d'"
    curs = conn.cursor()
    curs.execute(sql%(data))
    conn.commit()
    print('成功修改{}条数据'.format(curs.rowcount))


def delData(id):
    conn = getConnect("localhost", "root", "root", "shop", "utf8")
    sql = "delete from commoditytype where ct_id = '%d'"
    curs = conn.cursor()
    curs.execute(sql % id)
    conn.commit()
    print('成功修改{}条数据'.format(curs.rowcount))


modifyData(('xasdfxsdfx',1))
delData(1)