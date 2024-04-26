################################################
## 국방신문 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace

import urllib3
urllib3.disable_warnings()

pageLimit = 67
articleNumPerPage = 20

f = open('./mil_news_data_raw.txt', 'w')

for pageNum in range(1, pageLimit): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))
    
    # 한글은 이렇게 인코딩되어 나타남
    res = requests.get(f"https://www.gukbangnews.com/news/articleList.html?page={pageNum}&total=1359&box_idxno=&sc_section_code=S1N1&sc_sub_section_code=&sc_serial_code=&sc_area=&sc_level=&sc_article_type=&sc_view_level=&sc_sdate=&sc_edate=&sc_serial_number=&sc_word=&sc_multi_code=&sc_is_image=&sc_is_movie=&sc_user_name=&sc_order_by=E&view_type=sm", verify=False)
    htmlCode = res.text
    soup = BeautifulSoup(htmlCode, 'html.parser')

    
    for articleNum in range(1, articleNumPerPage+1):
        selectElement = '#section-list > ul > li:nth-child('+str(articleNum)+') > div > h4 > a'
        titleList = soup.select(selectElement)
        for title in titleList:
            articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

f.close()