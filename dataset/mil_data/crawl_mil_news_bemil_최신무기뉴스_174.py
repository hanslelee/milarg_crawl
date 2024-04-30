################################################
## Bemil 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

# import chardet

pageLimit = 6
articleNumPerPage = 30
# articleNumPerPage = 22

f = open('./mil_news_data_bemil_news.txt', 'a', encoding='utf-8')

for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))
    
    
    res = requests.get(f"https://bemil.chosun.com/nbrd/bbs/list.html?b_bbs_id=10180&branch=&pn={pageNum}", verify=False)
    
    htmlCode = res.content.decode('euc-kr', 'replace').encode('utf-8','replace')
    soup = BeautifulSoup(htmlCode, 'html.parser')

    
    for articleNum in range(1, articleNumPerPage+1):
        selectElement = f'#container-area > div.area.subpage > div.news_zone_01 > div.news_zone_01_01 > section > div.pcpadonly > table > tbody > tr:nth-child({articleNum}) > td:nth-child(2) > a:nth-child(1)'
        
        titleList = soup.select(selectElement)
        count=0
        for title in titleList:
            count+=1
            
            articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

f.close()