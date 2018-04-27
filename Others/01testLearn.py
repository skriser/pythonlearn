#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/04/27 2018/4/27 13:12
@author: 柴顺进
@file: 01testLearn.py 
@software:rongda
@note: python第一部分测试练习
"""  
# 2、给定一个整数N，判断N是否为素数
N = 191
x = N//2
while x > 1:
    if N % x == 0:
        print N, "NO A PRIME"
        break
    else:
        x -= 1
    print "X is ", x
else:
    print N, "IS A prime"
print 1/4
print (1/4+2.75)

# 11、使用while输出 [1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 0
list1 = []
while count < 9:
    count += 1
    list1.append(count)
print list1

# 12、使用while 将一个已知 list1=[] 进行赋值，得出 [1, 3, 5, 7, 9]
count1 = 0
list2 = []
while count1 < 9:
    count1 += 1
    if count1 % 2 != 0:
        list2.append(count1)
print list2

# 13、使用while输出1-100内的质数 ，类似于 2,3,5,7,11,13....
x = 1
while x < 100:
    tmp = x // 2
    while tmp > 1:
        if x % tmp == 0:
            break
        else:
            tmp -= 1
    else:
        print x,
    x += 1

