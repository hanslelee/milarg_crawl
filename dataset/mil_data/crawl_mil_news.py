################################################
## 국방논단 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

pageLimit = 700
articleNumPerPage = 7 * 700
# articleNumPerPage = 10

f = open('./mil_news_data_raw.txt', 'w')

# 한글은 이렇게 인코딩되어 나타남
res = requests.get("https://kookbang.dema.mil.kr/newsWeb/m/ATCE_CTGR_0010010000/list.do", verify=False)

htmlCode = res.text
soup = BeautifulSoup(htmlCode, 'html.parser')

# newsTitleTagList = soup.select('.news_tit')

for articleNum in range(1, articleNumPerPage+1):
    # selectElement = '#content > div.table_web > div.table_area > table > tbody > tr:nth-child('+str(articleNum)+') > td.alignl.subject > a'
    selectElement = '#listForm > ul > li:nth-child('+str(articleNum)+') > a > div.basic_list_1 > div.tit > h3'
    
    titleList = soup.select(selectElement)
    for title in titleList:
        articleTitle = title.text
        # articleTitle = eraseSpace(title.text)

        f.write('국방\t' + articleTitle + '\n')
        print(articleTitle)

f.close()