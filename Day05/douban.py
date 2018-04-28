# -*- encoding:utf-8 -*-
import requests
import re
import xlwt
from bs4 import BeautifulSoup

# 设置页码变量,以及总电影数量变量
page_num=0
alllist_num=0
# 设置全局datalist变量
datalist=[]
# 设置获取每页内容的方法
def get_each_page(i):
    global page_num,alllist_num
    url = "https://movie.douban.com/top250?start="+str(i*25)
    page_num = i + 1
    alllist_num=page_num*25
    r = requests.get(url,{"User-agent":"Mozilla/4.0"})
    soup = BeautifulSoup(r.text,"html.parser")
    return soup

# 设置处理html内容的方法
def getData(i):
    # 1、存储soup对象
    eachsoup = get_each_page(i)
    # 2、获取电影列表父元素
    movieList = eachsoup.find('ol',attrs={'class':'grid_view'})
    # 3、用循环处理所有li内的具体内容
    for movieLi in movieList.find_all('li'):
        data = []
        # 3.1、获取电影名
        movieName = movieLi.find('div',attrs={'class':'hd'}).find('span',attrs={'class':'title'}).getText()
        data.append(movieName)
        #3.2、获取电影评分
        movieScore = movieLi.find('div',attrs={'class':'bd'}).find('span',attrs={'class':'rating_num'}).getText()
        data.append(movieScore)
        #3.3、获取电影的评价人数
        movieEval=movieLi.find('div',attrs={'class':'star'})
        movieEvalNum=re.findall(r'\d+',str(movieEval))[-1]
        # 将电影的评价人数加入data
        data.append(movieEvalNum)
        #3.4、获取电影的短评
        movieQuote = movieLi.find('span', attrs={'class': 'inq'})
        if(movieQuote):
            # 将电影的短评加入data
            data.append(movieQuote.getText())
        else:
            data.append("无")
        datalist.append(data)
    return

#设置将数据保存至excel文档的方法
def savaData(savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('豆瓣最受欢迎影评TOP榜',cell_overwrite_ok=True)
    col = (u'电影名称', u'评分', u'评论人数', u'短评')
    for i in range(0, 4):
        sheet.write(0, i, col[i])  # 表格中书写列名
    for i in range(0, alllist_num):  # 总共250条影评
        data = datalist[i]
        for j in range(0, 4):
            sheet.write(i + 1, j, data[j])  # 给表格添加数据
    book.save(savepath)  # 保存excel
    return

# 设置主方法
# 参数分别是：访问的页数，以及存储的文件名
def doMain(pageNum,filename):
    for j in range(0, pageNum):
        getData(j)
    savaData(filename)
    return
# 执行主函数
doMain(5,"douban.xls")