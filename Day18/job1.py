# 导入一些工具包
import requests
from lxml import etree
import pymysql



#一、获取链接对象
connect = pymysql.connect(host="localhost",\
user="root",password="123123",\
db="51job",charset="utf8")
#二、获取游标对象
cursor = connect.cursor()

jobInfoAll = []
# 确定一个对象，即网址，关键词：数据分析师
for i in range(1, 6):
    url = "http://search.51job.com/list/010000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590%25E5%25B8%2588,2," + str(
        i) + ".html"
    res = requests.get(url)
    res.encoding = 'gbk'
    # 定义一个节点树的根
    root = etree.HTML(res.text)
    # 利用xpath查找网页信息
    position = root.xpath('//div[@class="el"]/p/span/a/@title')
    company = root.xpath('//div[@class="el"]/span/a/@title')
    place = root.xpath('//div[@class="el"]/span[@class="t3"]/text()')
    salary = root.xpath('//div[@class="el"]/span[@class="t4"]/text()')
    #print("第{}页有{}个职位".format(i,len(position)))
    # 把取出的信息放到数据框
    #print([position, company, place, salary])
    k = 1
    for pos,com,loc,sal in zip(position,company,place,salary):
        #将每一条职位信息都添加到mysql数据库中
        sql = "insert into jobs values('%s','%s','%s','%s')"
        cursor.execute(sql%(pos,com,loc,sal))
        
        #提交sql
        connect.commit()
        print("添加第{}数据成功：{}".format((i-1)*50+k,cursor.rowcount))
        jobInfoAll.append((pos,com,loc,sal))
        #print(pos,com,loc,sal)  #pos:职位名,com:公司名,loc:地点,sal:薪资
        #print("***************************")
        k+=1

print(len(jobInfoAll))  #1~5页的所有职位信息

fields = ['职位名', '公司名', '地点', '薪资']