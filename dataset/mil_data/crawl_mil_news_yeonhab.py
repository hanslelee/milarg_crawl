################################################
## 국방신문 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

pageLimit = 20
articleNumPerPage = 25
# articleNumPerPage = 22

f = open('./mil_news_data_yeonhab_raw.txt', 'w')

for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))
    
    # 한글은 이렇게 인코딩되어 나타남
    res = requests.get(f"https://www.yna.co.kr/politics/defense/{pageNum}", verify=False)
    htmlCode = res.text
    soup = BeautifulSoup(htmlCode, 'html.parser')

    
    for articleNum in range(1, articleNumPerPage+2):
        selectElement = f'#container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child({articleNum}) > div > div.news-con > a > strong'
        #container > div > div > div.section01 > section > div.list-type038 > ul > li:nth-child(25) > div > div.news-con > a > strong
        
        titleList = soup.select(selectElement)
        for title in titleList:
            articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

f.close()