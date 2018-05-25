#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/24 10:11
@author: 柴顺进
@file: teacherCode.py 
@software:rongda
@note: 
"""  
f = open("./data.csv")  #f是一个可迭代对象
result = [] #空列表，用于存放每一行的数据
for line in f:
    # result.append(line)
    row = line.split(",")  #将每一行数据用","分割,保存到一个列表中
    data = []
    for word in row:
        #print(word.strip())#去除每一行数据中多余的空格
        data.append(word.strip())
    result.append(data)
# print(result)
f.close()
print(result)

#创建一个output.csv文件，将数据写入到其中
with open("./output.csv","w") as csvFile:
    result.append(["Jack","104"])
    for row in result:
        #将一个列表中的数据用","拼接成一个字符串
        csvFile.write(",".join(row)+"\n")  #"name,stuNo"  "Zhangsan,101"
    csvFile.close()



