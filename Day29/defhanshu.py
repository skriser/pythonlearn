#!usr/bin/env python  
# -*- coding:utf-8 -*-
""" 
@time: 2018/06/05 15:09
@author: 柴顺进
@file: defhanshu.py 
@software:rongda
@note: 
"""
import random
import re
import urllib2

# 设置函数 获取页面内容
import chardet
import xlwt


def getHtml(url):
    USER_AGENTS = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/531.21.8 (KHTML, like Gecko) Version/4.0.4 Safari/531.21.10",
        "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/533.17.8 (KHTML, like Gecko) Version/5.0.1 Safari/533.17.8",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/533.19.4 (KHTML, like Gecko) Version/5.0.2 Safari/533.18.5",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-GB; rv:1.9.1.17) Gecko/20110123 (like Firefox/3.x) SeaMonkey/2.0.12",
        "Mozilla/5.0 (Windows NT 5.2; rv:10.0.1) Gecko/20100101 Firefox/10.0.1 SeaMonkey/2.7.1",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.8 (KHTML, like Gecko) Chrome/4.0.302.2 Safari/532.8",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_4; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.464.0 Safari/534.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.13 (KHTML, like Gecko) Chrome/9.0.597.15 Safari/534.13",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.186 Safari/535.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
        "Mozilla/5.0 (Macintosh; U; Mac OS X Mach-O; en-US; rv:2.0a) Gecko/20040614 Firefox/3.0.0 ",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.0.3) Gecko/2008092414 Firefox/3.0.3",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1) Gecko/20090624 Firefox/3.5",
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.6; en-US; rv:1.9.2.14) Gecko/20110218 AlexaToolbar/alxf-2.0 Firefox/3.6.14",
        "Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; en-US; rv:1.9.2.15) Gecko/20110303 Firefox/3.6.15",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1"
    ]
    # 代理的IP设置
    proxies = ['114.215.95.188:3128', '218.14.115.211:3128']
    req = urllib2.Request(url)
    # 设置消息头
    req.add_header('User-Agent', random.choice(USER_AGENTS))
    # 设置代理ip地址
    proxy_support = urllib2.ProxyHandler({"http": random.choice(proxies)})
    opener = urllib2.build_opener(proxy_support)
    urllib2.install_opener(opener)
    # 访问并获取服务端返回的对象
    times = 0
    try:
        res = urllib2.urlopen(req)
        html = res.read()
        return html
    except:
        times += 1
        getHtml(url)

# 设置正则处理页面对象
# def getDataList(jobname,pagenumber):
#     url = "https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(jobname,pagenumber)
#     html = getHtml(url)
#     code = chardet.detect(html)['encoding']
#     html = html.decode(code).encode('utf-8')
#     print html
#     # 02.设置正则
#     regstr = '<p class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>'
#     reg = re.compile(regstr, re.S)
#     # 03. 获取结果
#     result = re.findall(reg, html)
#     print result
#     return result
def getDataList(jobname,num):
    # 01.获取51job网页内容
    # url = "https://search.51job.com/list/000000,000000,0000,00,9,99," + str(jobname) + ",2,"+str(num)+".html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=4&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=".format(jobname,num)
    # print
    html = getHtml(url)
    # 使用chardet模块，获取网页对象的编码，进行转码
    # code = chardet.detect(html)['encoding']
    html = html.decode('gbk').encode('utf-8')
    # print html
    # 设置正则表达式
    reg = re.compile(
        r'<p class="t1 ">.*?<a target="_blank" title="(.*?)".*?<span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*?<span class="t5">(.*?)</span>',
        re.S)
    result = re.findall(reg, html)
    return result

dataList = []

# 向全局dataList添加数据
def dealDataList(jobname,pagenumber):
    global dataList
    # 根据设置的页数执行多次获取数据
    for k in range(pagenumber):
        data = getDataList(jobname,k+1)
        for i in data:
            dataList.append(i)
# 设置存储的函数
def saveExecl(jobname,filename):
    #保存到本地
    # 04. 打开workbook
    book = xlwt.Workbook(encoding='utf-8')
    # 05.创建工作表
    sheet = book.add_sheet(jobname)
    # 06.存入第一行
    col = ('职位名', '公司名', '工作地点', '薪资', '发布时间')
    for i in range(len(col)):
        sheet.write(0, i, col[i])
    for i in range(len(dataList)):
        for j in range(len(dataList[i])):
            sheet.write(i + 1, j, dataList[i][j])

    # 07. 存储到文件
    book.save(filename)

def saveTxt(filename):
    for i in range(len(dataList)):
        data = dataList[i]
        with open(filename,'a') as f:
            f.write(data[0]+"\t"+data[1]+"\t"+data[2]+"\t"+data[3]+"\t"+data[4]+"\n")
            f.close()
def main(jobname, pagenumber,filename):
    dealDataList(jobname,pagenumber)

    if 'txt' in filename:
        saveTxt(filename)
    if 'xls' in filename:
        saveExecl(jobname, filename)


main('c', 2, 'c.txt')