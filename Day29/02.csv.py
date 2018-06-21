# -*- coding:utf-8 -*-
import csv
# 1. 打开文件，如果不存在，就新建一个 w 代表 write
with open('csvExample/csvtest.csv','w') as csvfile:
# 2. 用变量存储
    writer = csv.writer(csvfile)
# 3. row 行  写入行 信息   writerow（）  注意没有s写入的是单行
    writer.writerow(['id', 'url', 'keywords'])
# 4. 存入多个数据  ，就是把每行要写的，存入某个列表内，
# 通过  writerows （）批量写入
    data = [('1', 'http://www.xiaoheiseo.com/', '小黑'),
            ('2', 'http://www.baidu.com/', '百度'),
            ('3', 'http://www.jd.com/', '京东')]
    writer.writerows(data)

# 1. 格式对齐都在with下的
# 2. 文件夹要有
# 3. writer.writerows(data)不要写到外面的
