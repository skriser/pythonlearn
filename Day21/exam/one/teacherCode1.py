#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/24 10:11
@author: 柴顺进
@file: teacherCode1.py 
@software:rongda
@note: 
"""  
import csv

def getData(path):  #path代表读取文件的路径
    result = []
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            newRow = {}
            # row.keys()  ["   name","   stuNo"]
            # row.values()  ["ZhangSan","101"]
            for key,value in zip(row.keys(),row.values()):
                newRow[key.strip()] = value.strip()
            result.append(newRow)
    return result
# data = getData("./data.csv")
# print(data)
with open("./output.csv","w") as csvFile:
    data = getData("./data.csv")
    data.append({"name":"Jack","stuNo":"104"})
    #用csv模块的dictwrite方法将字典写入到csv文件
    fields = ["name","stuNo"]
    writer = csv.DictWriter(csvFile,fieldnames=fields)
    #将csv文件的第一行（即列名写入到csv文件）
    writer.writeheader()
    #遍历数据，将字典写入到csv文件中
    for row in data:
        writer.writerow(row)
    csvFile.close()


def getData(path):  #path代表读取文件的路径
    with open(path) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(dict(row))

getData("./data.csv")
