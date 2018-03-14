# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import os
import re
import datetime
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigdata_crawling.settings")
import django
django.setup()
from community.models import Community,Test

def spider(page_max):
    
    review_list = []
    review_list2 = []
    page = 2
    date1 = []
    cName = "Clien"
    tName = "모두의 공원"
    conType = "글제목"

    while page< page_max :
        url = 'https://www.clien.net/service/board/park?&od=T31&sk=title&sv=노트7&articlePeriod=2017&po='+ str(page)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text, 'html.parser')
        
        h=0
        for link in soup.select('div.list-title > a'):
            title = link.string
            #print(title)
            review_list.append(link.get_text().strip())
            h=h+1
        i=0   
        for time in soup.select('div.list-time > span.time > span.timestamp'):   
            times = time.string
            date1 = times.split()
            date2 = date1[0]
            convert_date=datetime.datetime.strptime(date2,"%Y-%m-%d").date()
            #print(times)
            #print(convert_date)
            review_list2.append(convert_date)
            i=i+1

        # for j in range(0,len(review_list)):
        #     print(review_list[int(j)]+"   "+str(review_list2[int(j)]))
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
    print("est")
    blog_data_dict = spider(15)
    for t in blog_data_dict:
        #print(t[0])
        #print(t[1])
        #print(t[2])
        #print(t[3])
        #print(t[4])
        new_community = Community()
        new_community.cName=t[0]
        new_community.tName=t[1]
        new_community.conType=t[2]
        new_community.content=t[3]
        new_community.date=t[4]
        new_community.save()    