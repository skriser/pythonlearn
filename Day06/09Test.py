#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/05/02 2018/5/2 15:09
@author: 柴顺进
@file: 09Test.py 
@software:rongda
@note: 
"""
# # # 乘法口诀表
for i in range(1,10):
    for j in range(1,i+1):
        # 占位符通过整体来占位符
        print '%7s'%('|'+str(j)+ 'X'+str(i) + '= %2s'%str(j*i) + '|'),
    print

# #有个棋盘 64个方格，第一个
sum1 = 0
for i in range(64):
    sum1 = sum1 +0.00001*(2**i)
print sum1

# #3、公鸡3元每只，母鸡5元每只，小鸡1元3只，一百元钱买一百 只鸡。请求出公鸡，母鸡和小鸡的数目。
# 3x+5y+0.3z = 100
for a in range(33):
    for b in range(20):
        for c in range(100):
                    # 求小数的时候需要用上小数点
            if 3 * a + 5 * b + 1.0/3 * c == 100 and a + b + c == 100:
                print a, b, c

# 4、一个小孩买了价值少于1美元的糖，并将1美元的钱交给售货员。
# 售货员希望用数目最少的硬币找给小孩。假设提供了数目不 限的，
# 面值为2 5美分、1 0美分、5美分、及1美分的硬币，写一个算法让售货员用最少的硬币数找给小孩。
# 25x +10y +5z+w = 100
# use = raw_input("需要找零的总钱数：")

# for x in range(5):
#     for y in range(3):
#         for z in range(3):
#             for w in range(5):
#                 25*x +10*y+5*z +w == use
#
#
use = 77 #输入数
a = use // 25 # 25美分 要多少个币
b = (use % 25) // 10  #除去25美分 还剩多少 ，10美分要多少
c = ((use % 25) % 10) // 5 # 需要多少 5美分的
d = ((use % 25) % 10) % 5 # 剩下的就是1美分的
print 'a:'+str(a),'b:'+str(b),'c:'+str(c),'d:'+str(d)

# #5、小猴第一天摘下若干枣子，当即吃掉了一半，不过瘾又多吃了一个；
# 第二天吃了剩下的一半又多吃了一个；以后每一天都吃了前一天剩下的一半多一个。
# 到第十天小猴再想吃时，见到只剩 下一只枣子了。问第一天这堆枣子有多少？
# x /2 +1  (x -(x/2 +1))/2 +1
#   left = x - (x/2 + 1)
# 疑问：怎么把这个求解的循环给表示出来，循环方法在最后得到的答案是1 :这是一个递给数列，可以转换为数学数列求解：数列是前项和后项的关系，
# 这个数列是前后项的关系
i = 9
list1 = range(10)
list1[9] = 1
while i > 0:
    list1[i-1] = 2*list1[i] + 2
    i -= 1
print list1

# 直接推导，用第10次进行倒退
a = 1
for i in range(9):
    a = (a + 1)*2
print a
#
# j = 0
# list2 = range(10)
# list2[j] = 1534
# while j < 9:
#     list2[j+1] = list2[j] - (list2[j]/2 + 1 )
#     j += 1
# print list2


# 6、 一张纸的厚度大约是0.08mm，对折多少次之后能达到珠穆 朗玛峰的高度（8848.13米）？
# 1m = 100cm 1cm = 10mm 1m == 1000mm 8848.13m = 8848130mm
i = 0
while 8*(2**i) < 884813000:
    i += 1
else:
    print i

print 2**27*8 > 884813000

# 7.有一个列表，其中包括10个元素，例如 [1,2,3,4,5,6,7,8,9,0]要求将列表中的每个元素依次向前移动一个位置，将第一个元素到列表
# # 的最后，然后输出这个列表。最终的样式是[2,3,4,5,6,7,8,9,0,1]
list1 = range(10)
print(list1)
list1.append(list1.pop(0))
print(list1)

# 8.第一个月初有一对刚诞生的兔子，第二个月后（第三个月初）他们可以生育。每月每对可生育的兔子会诞生下一对新兔子，兔子永不死去；
# 求第21个月兔子的数量
dict1 = {1: 1, 2: 1, 3: 2, 4: 3, 5: 5, 6: 8}
list1 = [1]*25
for i in range(1, 20):
    list1[i+1] = list1[i] + list1[i-1]
print(list1)

# 判断条件时候用while，进行预测迭代的时候用for循环

a = 1
b = 0
for i in range(21):
    a, b = b, a+b
print(b)

print(24 * 179)
