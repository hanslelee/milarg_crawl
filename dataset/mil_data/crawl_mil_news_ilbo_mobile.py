################################################
## 국방일보 데이터 크롤링
################################################

import requests
from bs4 import BeautifulSoup
from utils import eraseSpace
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import urllib3
urllib3.disable_warnings()


articleNumPerPage = 49000
# articleNumPerPage = 20


f = open('./mil_news_data_ilbo.txt', 'w')

# 한글은 이렇게 인코딩되어 나타남
res = requests.get("https://kookbang.dema.mil.kr/newsWeb/m/ATCE_CTGR_0010010000/list.do", verify=False)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://kookbang.dema.mil.kr/newsWeb/m/ATCE_CTGR_0010010000/list.do")

htmlCode = res.text

soup = BeautifulSoup(htmlCode, 'html.parser')

for articleNum in range(1, articleNumPerPage+1):
    print('articleNum : '+str(articleNum))

    if (articleNum-1)%10 == 0:
        driver.find_element(By.XPATH, '//*[@id="more_gisa"]').click()
        time.sleep(2)
        
        page_source = driver.page_source

        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(page_source, 'html.parser')
    
    selectElement = '#listForm > ul > li:nth-child('+str(articleNum)+') > a > div.basic_list_1 > div.tit > h3'
    #listForm > ul > li:nth-child(20) > a > div.basic_list_1 > div.tit > h3
    
    #container > div > div.article_body > div.article_body_main > ul > li:nth-child(2) > a > div.txt > h3
    #container > div > div.article_body > div.article_body_main > ul > li:nth-child(1) > a > div > h3
    
    
    titleList = soup.select(selectElement)
    
    for title in titleList:
        articleTitle = title.text

        f.write('국방\t' + articleTitle + '\n')
        print(articleTitle)

        

f.close()