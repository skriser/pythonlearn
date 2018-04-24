#!usr/bin/env python  
#-*- coding:utf-8 *-
""" 
@time: 2018/04/24 2018/4/24 9:28
@author:chaishunjin 
@file: 02Print.py 
@software:rongda
"""  

# print "打印一个整数" + str(4)
# print(4)
## 直接都是字符串
# str1 = '罚抄'
# str2 = '3'
# str3 = '遍'
# print str1+str2+str3
#
# str1 = '罚抄'
# str2 = 3
# str3 = '遍'
##使用反引号转义
# print str1+`str2`+str3
##使用string方法进行数据类型转换
# print str1+str(str2)+str3

#格式化输出
# #1.字符串占位符 %s
# print "His name is %s"%"jack"
# #2.整数占位符 %d
# print "He is %d years old"%20
# #3.浮点占位符 %f
# print "His weight is %f kg"%180.2
# print "His weight is %.3f kg"%180.2
# #4.指定占位符宽度 通过%[-左对齐][数值指定宽度]s
# print "Name:%10s Age:%8d Height:%8.2f"%("jack",25,183)
# #使用左对齐 “-”打印格式统一好看
# print "Name:%-10s Age:%-8d Height:%-8.2f"%("jackoqdfa",25,183)
# print "Name:%-10s Age:%-8d Height:%-8.2f"%("jacsafk",25,183)
# print "Name:%-10s Age:%-8d Height:%-8.2f"%("jasdddsack",25,183)
# print "Name:%-10s Age:%-8d Height:%-8.2f"%("zxck",25,183)

# #格式化的顺序是一致的
# print "%s is %d years old"%("jack",20)
# # print "%d is %d years old"%("jack",20)
# print "%s is %s years old"%("jack",20)
#
# print "{0} is {1} years old".format("jack",20)
# print "{1} is {0} years old".format(20,"jack")

#设置格式化，把三个变量指定宽度
mat = "{:20}\t{:28}\t{:32}"
#设置格式化，把三个变量指定宽度，并设置为居中
mat1 = "{:^20}\t{:^28}\t{:^32}"
print mat.format("asdfa","asdf","sds")
print mat1.format("asdfa","asdf","sds")
# boy  = ["jack",20]
# girl = ["Miki",18]
# print "{0[0]} is {0[1]} years old,{1[0]} is {1[1]} years old ".format(boy,girl)