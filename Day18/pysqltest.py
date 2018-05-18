#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/17 14:52
@author: 柴顺进
@file: pymysql.py 
@software:rongda
@note:
四、编写python代码，实现如下要求：
    (1)请写出python访问mysql数据库的主要步骤

    (2)分别在学生表和成绩表中添加两位学生的信息
        学生表:
        '09' , 'Jace' , '1993-05-20' , '男'
        '10' , 'Rose' , '1992-06-14' , '女'

        成绩表：
        Jace        语文：98    数学：78    英语90
        Rose        语文：85    数学：88    英语：89
insert into score (
(SELECT sno from students WHERE sname = 'jace';),
(SELECT cno from course WHERE course.cname='语文';)
,98
)
    (3)查询除学生的各科成绩，写入到excel表中
"""  
import pymysql
import openpyxl
conn = pymysql.connect(host="localhost",user="root",password="root",charset="utf8",db="school")
cursors = conn.cursor()


def insertSchool(conn, cursors):
    judge_insert = "select sno from students where sno = '10';"
    if cursors.execute(judge_insert):
        return
    sql_student = "insert into students VALUES ( '09' , 'Jace' , '1993-05-20' , '男'),( '10' , 'Rose' , '1992-06-14' , '女');"
    cursors.execute(sql_student)
    conn.commit()
    sql_stuNo = "SELECT sno from students WHERE sname = '%s';"
    sql_couNo = "SELECT cno from course WHERE course.cname='%s';"
    sql_score = "insert into score VALUES ('%s','%s',%d)"

    dict1 = {'Jace': {'语文':98, '数学': 78, '英语': 90}, 'Rose': {'语文':85, '数学': 88, '英语': 89}}
    for i in dict1.keys():
        cursors.execute(sql_stuNo % i)
        sql_sno = cursors.fetchone()
        for j in dict1.get(i).keys():
            cursors.execute(sql_couNo % j)
            sql_cno = cursors.fetchone()
            sql_score1 = dict1.get(i).get(j)
            print(sql_sno[0], sql_cno[0], sql_score1)
            cursors.execute(sql_score % (sql_sno[0], sql_cno[0], sql_score1))
            conn.commit()


def saveExcel(cursors,filename=None):
    sql_all = "SELECT s.sno,s.sname,r.cname,c.score from students s LEFT JOIN score c on s.sno = c.sno LEFT JOIN course r on r.cno = c.cno" \
              " order by s.sno;"
    cursors.execute(sql_all)
    data = cursors.fetchall()
    title = cursors.description
    list_title = []
    for i in title:
        list_title.append(i[0])
    list_data = [list_title]
    for i in data:
        list_data.append(i)
    workbooks = openpyxl.Workbook()
    worksheets = workbooks.active
    for i in list_data:
        worksheets.append(i)
    workbooks.save('mysqltest.xlsx')


insertSchool(conn, cursors)
saveExcel(cursors)
cursors.close()
conn.close()
