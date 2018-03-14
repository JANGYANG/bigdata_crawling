# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import requests
from bs4 import BeautifulSoup
import os
import re
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigdata_crawling.settings")
import django
django.setup()
from community.models import Community, Test


def spider():
    
    review_list=[]
    review_list2=[]
    page = 1000
    cName = "ExtremeMovie"
    tName = "영화수다"
    conType = "글제목"
    countnotice = 3
    countbest = 7
    count = countnotice + countbest
    while page< 3000:
        url = 'http://extmovie.maxmovie.com/xe/index.php?mid=movietalk&page='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        plain_text1 = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        soup1 = BeautifulSoup(plain_text1, 'html.parser')
        
        h = 0
        for link in soup.select('tbody > tr > td.title > a'):
            if (h>2*(count-1)):
                title = link.string
                regex = bool(re.search("\(\d+\)",title))
                if regex != True:
                    review_list.append(link.get_text().strip())
            h = h+1
        
        i = 0
        l = len(soup1.select('tbody > tr > td:nth-of-type(4)'))
        for p in range(count,l):
            link1 = soup1.select('tbody > tr > td:nth-of-type(4)')[p]
            title1= link1.get_text().strip()
            regex = bool(re.search("\d+\.\d+\.\d+",title1))
            if regex == True :
                convertdate = datetime.datetime.strptime(title1, "%Y.%m.%d").date()
                review_list2.append(convertdate)
        
        page += 1
    
    data = []
    index = 0
    for k in range(0,len(review_list)):
        data2 = []
        data2.append(cName)
        data2.append(tName)
        data2.append(conType)
        data2.append(review_list[int(k)])
        data2.append(review_list2[int(k)])
        # data[index][0] = cName
        # data[index][1] = tName
        # data[index][2] = conType
        # data[index][3] = content
        # data[index][4] = dateInput
        # data[index]["cName"] = cName
        # data[index]["tName"] = tName
        # data[index]["conType"] = conType
        # data[index]["content"] = content
        # data[index]["date"] = dateInput
        data.append(data2)
        index += 1
        
    return data

if __name__ == '__main__':
    data3=spider()
    for t in data3:
        # print(t[0])
        # print(t[1])
        # print(t[2])
        # print(t[3])
        # print(t[4])
        new_community = Community()
        new_community.cName=t[0]
        new_community.tName=t[1]
        new_community.conType=t[2]
        new_community.content=t[3]
        new_community.date=t[4]
        new_community.save()
                
# def parse_community():
#     req = requests.get('http://www.fmkorea.com/index.php?mid=best&page=30')
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')
    
   
#     content = soup.select(
#         'ul > li > div.li > h3 > a'
#     )
    
#     cName = "FmKorea"
#     tName = "title"
#     conType = "type"
    
    
#     date = soup.select(
#         'div.li > div > span.regdate'
#     )
#     data = []
#     index = 0
#     for content in content:
#         data2 = []
#         data2.append(cName)
#         data2.append(tName)
#         data2.append(conType)
#         data2.append(content)
#         data2.append(date)
#         # data[index][0] = cName
#         # data[index][1] = tName
#         # data[index][2] = conType
#         # data[index][3] = content
#         # data[index][4] = dateInput
#         # data[index]["cName"] = cName
#         # data[index]["tName"] = tName
#         # data[index]["conType"] = conType
#         # data[index]["content"] = content
#         # data[index]["date"] = dateInput
#         data.append(data2)
#         index += 1
        
#     return data


# if __name__ == '__main__':
#     for n in range(4,5):        
#         blog_data_dict = parse_community()
#         for t in blog_data_dict:
#             print(t[0])
#             print(t[1])
#             print(t[2])
#             print(t[3])
#             print(t[4])
#             # new_community = Community()
#             # new_community.cName=t[0]
#             # new_community.tName=t[1]
#             # new_community.conType=t[2]
#             # new_community.content=t[3]
#             # new_community.date=t[4]
#             # new_community.save()
#             # Community(cName=t[0],tName=t[1],conType=t[2],content=t[3],date=t[4]).save()
#             # Community(cName=t["cName"],tName=t["tName"],conType=t["conType"],content=t["content"],date=t["date"]).save()