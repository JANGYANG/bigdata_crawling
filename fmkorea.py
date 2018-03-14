# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import requests
from bs4 import BeautifulSoup
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigdata_crawling.settings")
import django
django.setup()
from community.models import Community


def parse_community(n):
    req = requests.get('http://www.fmkorea.com/index.php?mid=best&page='+str(n))
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    
   
    content = soup.select(
        'ul > li > div.li > h3 > a'
    )
    
    cName = "fmkorea"
    
    tName = soup.select(
        'ul > li > div.li > div > span.category'
    )
    conType = "title"
    
    
    date = soup.select(
        'div.li > div > span.regdate'
    )
    data = []
    index = 0
    for content in content:
        dateInput = date[index].text
        dateInput = dateInput.replace(".","-")
        dateInput = re.sub('\s+', '', dateInput)
        contentInput = content.text
        contentInput = re.sub('\s+','', contentInput)
        data2 = []
        data2.append(cName)
        data2.append(tName[index].text)
        data2.append(conType)
        data2.append(contentInput)
        data2.append(dateInput)
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
    # 4983
    for n in range(18,4983):
        blog_data_dict = parse_community(n)
        for t in blog_data_dict:
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
            # Community(cName=t[0],tName=t[1],conType=t[2],content=t[3],date=t[4]).save()
            # Community(cName=t["cName"],tName=t["tName"],conType=t["conType"],content=t["content"],date=t["date"]).save()
