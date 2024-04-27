################################################
## 국방논단 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

pageLimit = 223
articleNumPerPage = 10

f = open('./mil_news_part.txt', 'w')

for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))
    
    res = requests.get(f"https://www.kida.re.kr/frt/board/frtNormalBoard.do?searchCondition=auther&searchKeyword=&pageIndex={pageNum}&depth=2&sidx=245&stype=&v_sidx=", verify=False)
    
    htmlCode = res.text
    soup = BeautifulSoup(htmlCode, 'html.parser')

    # newsTitleTagList = soup.select('.news_tit')
    
    for articleNum in range(1, articleNumPerPage+1):
        selectElement = f'#content > div.table_web > div.table_area > table > tbody > tr:nth-child({articleNum}) > td.alignl.subject > a'
        
        titleList = soup.select(selectElement)
        for title in titleList:
            articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

f.close()