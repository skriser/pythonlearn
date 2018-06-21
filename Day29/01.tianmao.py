# -*- coding:utf-8 -*-
import re
import xlwt
from getHtml import getHtml

# 01.获取天猫页的内容
url = 'https://www.tmall.com'
html = getHtml(url)
print html
# 02. 设置正则表达式
href="//list.tmall.com/search_product.htm?from=mallfp..pc_1.0_hq&click_id=针织衫&q=针织衫"
reg = re.compile('<a href="(.*)">(.*)</a>')
links = re.findall(reg,html)
print len(links)
# 存入本地excel
# 01.获取工作簿对象,别忘了设置编码，或者下面的字符串加上  u'天猫'
wbk = xlwt.Workbook(encoding='utf-8')
# 02.创建一个工作表
sheet = wbk.add_sheet('天猫')
# 03.设置第一行的内容
col = ('编号', '链接', '内容')
for i in range(len(col)):
    sheet.write(0, i, col[i])

# 04.设置 存入本地的序号
for i in range(len(links)):
    sheet.write(i+1,0,i+1)
    for j in range(len(links[i])):
        sheet.write(i+1,j+1,links[i][j])

# 05. 存储到文件
wbk.save('tianmao.xls')




