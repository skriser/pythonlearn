#!usr/bin/env python  
#-*- coding:utf-8 *-
""" 
@time: 2018/04/24 2018/4/24 13:05
@author:chaishunjin 
@file: 04List.py 
@software:rongda
@note: 列表的基本应用
"""  
# list1 = ['h','e','l','l','o']
# print list1
# list2 = list('hello')
# print list2
# print "list1[0]:",list1[0]
# print "list2[1:5]:",list2[1:5]
#
list3 = [1,2,3,'abc',5,6,7]
# print list3
# print id(list3)
# print id(list3[:]) #复制一份，这个说明内存中list不是唯一的，这么说在内存空间唯一的是string,int数据类型也是一致的；
##！！！疑问待解答；--->为什么list可以进行复制内存空间不唯一，但是string和int等类型只有一个内存空间
#最小内存存储基本数据类型，这些具有唯一性。

# #更新列表：
# list4 = [1,2,3,4]
# list4.append(5)#在结尾追加一个对象
# list4.append(list3) #在结尾追加一个对象
# list4.append(6)
# print list4
# print list4[5][3]
# del list4[:]
# print list4
#
# #删除列表：
list5 = ['abc',123,456,'hello',[1,2,3]]

print 'hello'*4
print '2'*4
print 2*4
print ['Hi!']*4

