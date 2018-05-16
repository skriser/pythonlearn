#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/16 13:48
@author: 柴顺进
@file: 03connTest.py 
@software:rongda
@note: 
"""  
from Day17.connect import getConnect

conn = getConnect("localhost","root","root","shop","utf8")

curs = conn.cursor()
sql = "insert into students(`sNo`,`sName`,`sCourse`,`sResult`)" \
      "VALUES (1111,'jack','人工智能',99)"

curs.execute(sql)

conn.commit()
# rowcount 本次提交语句修改了几行数据
print('受影响的行数'+str(curs.rowcount))
