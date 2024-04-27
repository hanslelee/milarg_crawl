################################################
## 한겨래 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

pageLimit = 1691
articleNumPerPage = 15
# articleNumPerPage = 22

f = open('./mil_news_data_hangyeorae.txt', 'w')

for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))
    
    # 한글은 이렇게 인코딩되어 나타남
    res = requests.get(f"https://www.hani.co.kr/arti/politics/defense?page={pageNum}", verify=False)
    htmlCode = res.text
    soup = BeautifulSoup(htmlCode, 'html.parser')

    
    for articleNum in range(1, articleNumPerPage+1):
        selectElement = f'#__next > div > div > div.section_inner__Gn71W > div.section_flexInner__jGNGY.section_content__CNIbB > div.section_left__5BOCT > div > ul > li:nth-child({articleNum}) > article > a > div > div.BaseArticleCard_title__TVFqt'
        #__next > div > div > div.section_inner__Gn71W > div.section_flexInner__jGNGY.section_content__CNIbB > div.section_left__5BOCT > div > ul > li:nth-child(15) > article > a > div > div.BaseArticleCard_title__TVFqt

        titleList = soup.select(selectElement)
        for title in titleList:
            articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

f.close()