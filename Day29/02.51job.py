# -*- coding:utf-8 -*-
from getHtml import getHtml
import re
import xlwt
import chardet
# 01.获取51job网页内容
url = "https://search.51job.com/list/000000,000000,0000,00,9,99,python,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
html = getHtml(url)
code = chardet.detect(html)['encoding']

html = html.decode(code).encode('utf-8')

# 02.设置正则
reg = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)

#03. 获取结果
result = re.findall(reg,html)
print len(result)

# 04. 打开workbook
book = xlwt.Workbook(encoding='utf-8')
#05.创建工作表
sheet = book.add_sheet('python职位')
# 06.存入第一行
col = ('职位名','公司名','工作地点','薪资','发布时间')
for i in range(len(col)):
    sheet.write(0,i,col[i])
for i in range(len(result)):
    for j in range(len(result[i])):
        sheet.write(i+1,j,result[i][j])

# 07. 存储到文件
book.save('51job.xls')

# 存储为txt
# for i in range(0, len(result)):
#     data = result[i]
#     with open('51job.txt', 'a') as f:
#         f.write(data[0] + '\t' + data[1] + '\t' + data[2] + '\t' + data[3] + '\t' + data[4] + '\n')
#         f.close()