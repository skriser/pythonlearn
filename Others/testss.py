#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/25 10:10
@author: 柴顺进
@file: testss.py 
@software:rongda
@note: 
"""  

import os

from PIL import Image

# im = Image.open("captcha.gif")
# #(将图片转换为8位像素模式)
# im = im.convert("P")
#
# #打印颜色直方图
# print(im.histogram())
#
# his = im.histogram()
# values = {}
#
# for i in range(256):
#  values[i] = his[i]
#
# for j,k in sorted(values.items(),key=lambda x:x[1],reverse = True)[:10]:
#  print(j,k)

from PIL import Image

im = Image.open("captcha.gif")
im = im.convert("P")
im2 = Image.new("P", im.size, 255)

for x in range(im.size[1]):
    for y in range(im.size[0]):
        pix = im.getpixel((y, x))
        if pix == 220 or pix == 227:  # these are the numbers to get
            im2.putpixel((y, x), 0)

# im2.show()


inletter = False
foundletter=False
start = 0
end = 0
letters = []

for y in range(im2.size[0]):
 for x in range(im2.size[1]):
  pix = im2.getpixel((y,x))
  if pix != 255:
   inletter = True
 if foundletter == False and inletter == True:
  foundletter = True
  start = y

 if foundletter == True and inletter == False:
  foundletter = False
  end = y
  letters.append((start,end))

 inletter=False
print(letters)


import hashlib
import time
import math

count = 0
for letter in letters:
 m = hashlib.md5()
 im3 = im2.crop(( letter[0] , 0, letter[1],im2.size[1] ))
 print("%s" %(time.time()))
 m.update((str(time.time())+str(count)).encode('utf-8'))
 im3.save("./%s.gif"%(m.hexdigest()))
 count += 1
