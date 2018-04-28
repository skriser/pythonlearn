# -*- encoding:utf-8 -*-
import urllib2
import re
import xlwt
#获取源码
def get_content(page,job_name):
    url = "http://search.51job.com/list/020000,000000,0000,00,9,99,"+job_name+",2,"+str(page)+".html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    response = urllib2.urlopen(url)
    html = response.read().decode('gbk').encode('utf-8')
    return html
# 获取满足正则表达式的爬取目标
def get(html):
    pattern = re.compile(r'class="t1 ">.*? <a target="_blank" title="(.*?)".*? <span class="t2"><a target="_blank" title="(.*?)".*?<span class="t3">(.*?)</span>.*?<span class="t4">(.*?)</span>.*? <span class="t5">(.*?)</span>',re.S)#匹配换行符
    result = re.findall(pattern,html)
    return result
#设置全局的datalist存储爬取的目标
datalist = []
#调用方法获取爬取内容存入datalist
def savaDataToDatalist(page_num,job_name):
    for page in range(1,page_num):
        html = get_content(page,job_name)
        for i in get(html):
            data = []
            for j in range(0,5):
                data.append(i[j])
            datalist.append(data)
    return
# 将数据保存到excel中
def saveDataToXLS(savepath):
    book = xlwt.Workbook(encoding='utf-8', style_compression=0)
    sheet = book.add_sheet('51job搜索的职位', cell_overwrite_ok=True)
    col = (u'职位', u'公司名称', u'公司地点',u'薪资',u'发布时间')
    for i in range(0, 5):
        sheet.write(0, i, col[i])  # 列名
    i=0

    for i in range(0,len(datalist)):
        data = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j, data[j])  # 数据
    book.save(savepath)  # 保存
    return
# 将数据保存到txt中
def saveDataToTXT(savepath):
    for i in range(0,len(datalist)):
        data = datalist[i]
        with open(savepath,'a') as f:
            f.write(data[0]+'\t'+data[1]+'\t'+data[2]+'\t'+data[3]+'\t'+data[4]+'\n')
            f.close()
    return


def savaAll(job_name,page_num,saved_file_name):
    savaDataToDatalist(page_num,job_name)
    if('txt' in saved_file_name):
        saveDataToTXT(unicode(saved_file_name,'utf8'))
    if('xls' in saved_file_name):
        saveDataToXLS(unicode(saved_file_name,'utf8'))
    return
# savaAll('c',2,'c.xls')

# saveDataToXLS('51job.xls')
# saveDataToTXT('51job.txt')
savaAll('人工智能',3,'人工智能职位信息.xls')