# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from selenium import webdriver
import os
import re
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bigdata_crawling.settings")
import django
django.setup()
from community.models import Community


# chrome_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'chromedriver')
# driver = webdriver.Chrome(executable_path=r"/chromedriver")


# chromedriver_loc = './chromedriver'
# driver = webdriver.Chrome(executable_path=chromedriver_loc)

driver = webdriver.C



# driver = webdriver.Chrome('./chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
#driver = webdrver.PhantomJS('')#PhantomJS의 위치
driver.find_element_by_name('id').send_keys('yyykkk22')
driver.find_element_by_name('pw').send_keys('spiderM!2')
#로그인 버튼 누르기
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

def spider(max_pages):
    eurang_list=[]
    eurang_list2=[]
    cName = "Eurang"
    tName = "도시Q&A"
    conType = "글제목"

    page = 451

    while page < max_pages :
        driver.get('http://cafe.naver.com/firenze?iframe_url=/ArticleList.nhn%3Fsearch.clubid=10209062%26search.menuid=275%26search.boardtype=Q%26search.questionTab=A%26search.totalCount=151%26search.page='+str(page))
        driver.switch_to_frame('cafe_main')
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        notices = soup.select( 'tr > td.board-list > span > span > a')
        time = soup.select('tr > td')
#main-area > div:nth-child(8) > form > table > tbody > tr:nth-child(1) > td:nth-child(4)

        for n in notices :
            title = n.text.strip()
            regex = bool(re.search("\[\d+\]",title))
            if regex != True :
                eurang_list.append(n.get_text().strip())

        for m in time:
            date1 = m.get_text().strip()
            regex2 = bool(re.search("\d+\.\d+\.\d+", date1))
            if regex2 == True :
                convertdate = datetime.strptime(date1, "%Y.%m.%d.").date()
                eurang_list2.append(convertdate)

        page += 1

    data = []
    index = 0
    for k in range(0,len(eurang_list)):
        data2 = []
        data2.append(cName)
        data2.append(tName)
        data2.append(conType)
        data2.append(eurang_list[int(k)])
        data2.append(eurang_list2[int(k)])
        data.append(data2)
        index += 1

    return data
if __name__ == '__main__':
    data3 = spider(453)
    for t in data3:
        print(t[0])
        print(t[1])
        print(t[2])
        print(t[3])
        print(t[4])
