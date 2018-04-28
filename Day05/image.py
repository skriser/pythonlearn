# -*- encoding:utf-8 -*-
# 方法，使用urllib.urlretrieve() 方法直接将远程数据下载到本地
import requests
from bs4 import BeautifulSoup
import urllib
import os

#看这里。把豆瓣搜索，明星在地址栏，对应的那个数字，填入下面str（）的括号内
address = str(1275620)

# 设置获取网页内容的函数
def getHtml(index,number):
    # url = "https://movie.douban.com/celebrity/1004572/photos/?type=C&start="+str(index)
    url = "https://movie.douban.com/celebrity/"+number+"/photos/?type=C&start=" + str(index)
    r = requests.get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11"})
    soup = BeautifulSoup(r.text, "html.parser")
    return soup

# 设置全局images变量
images = []
# 获取首页的图片数量
imgLen = len(getHtml(0,address).find('ul', attrs={'class': "poster-col3 clearfix"}).find_all('img'))
# 设置处理网页内容的函数
def getImages(pageNum,name,number):
    #创建文件夹
    if os.path.exists(name):
        os.rmdir("photos")
    else:
        os.mkdir(name)
    os.chdir(name)
    global address,images,imgLen
    for k in range(pageNum):
        # 1、存储soup对象
        eachsoup = getHtml(k*imgLen,number)
        # 2、获取图片列表父元素
        imageList = eachsoup.find('ul', attrs={'class': "poster-col3 clearfix"})
        # 3、获取所有image
        #     通过extend方法，还是一个list，如果用append会是多个list，下面的循环的就要额外处理了
        images.extend(imageList.find_all('img'))

    #3、用循环处理所有li内的具体内容
    for i in range(len(images)):
        try:
            #获取图片后缀名，防止真实网址图片为png，jpg，gif等格式
            suffix = images[i]['src'][-3:]
            image_name = str(i+1)+'.'+suffix
            urllib.urlretrieve(images[i]['src'],image_name)
        except Exception:
            print('存储有异常')
    return

# 看这里。
# 在这里可以控制存储几页，只需要在下面个getImages(1，'liyifei'，adress)的数字位置更改就行，1就是存一页图片，2就是存两页
#然后第二个位置填的是存储的文件夹的名字。注意，暂时你们就用拼音，并且用英文的引号引起来，不能有汉字，
# 再次运行，要用不同的文件夹名字，否则运行不了。
#当然这些问题，在后期都可以改善，咱们在这运行简单版的
getImages(5,'zhaoliying',address)