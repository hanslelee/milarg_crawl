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

# pageLimit = 6000
pageLimit = 7
articleNumPerPage = 7

f = open('./mil_news_data_ilbo.txt', 'w')

res = requests.get(f"https://kookbang.dema.mil.kr/newsWeb/ATCE_CTGR_0010010000/list.do", verify=False)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://kookbang.dema.mil.kr/newsWeb/ATCE_CTGR_0010010000/list.do")
htmlCode = res.text
soup = BeautifulSoup(htmlCode, 'html.parser')


for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))

    for articleNum in range(1, articleNumPerPage+1):
        if articleNum%2 == 1:
            selectElement = '#container > div > div.article_body > div.article_body_main > ul > li:nth-child('+str(articleNum)+') > a > div.txt > h3'
        else:
            selectElement = '#container > div > div.article_body > div.article_body_main > ul > li:nth-child('+str(articleNum)+') > a > div.txt > h3'

            

        print(selectElement)
        # if selectElement ==null:
        #1 //*[@id="container"]/div/div[3]/div[1]/ul/li[1]/a/div/h3
        #2 //*[@id="container"]/div/div[3]/div[1]/ul/li[1]/a/div[2]/h3
        #3 //*[@id="container"]/div/div[3]/div[1]/ul/li[1]/a/div/h3
        #4 //*[@id="container"]/div/div[3]/div[1]/ul/li[1]/a/div[2]/h3
        #5 //*[@id="container"]/div/div[3]/div[1]/ul/li[1]/a/div[2]/h3
        


        titleList = soup.select(selectElement)
        print(titleList)
        for title in titleList:
            articleTitle = title.text
            # articleTitle = eraseSpace(title.text)

            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)

        if (articleNum)%7 == 0:
            # xpath_ = f'/html/body/div[1]/div[2]/div/div[3]/div[1]/div/a[{pageNum%11+3}]'
            xpath_ = '//*[@id="container"]/div/div[3]/div[1]/div/a['+str((pageNum%11)+3)+']'
            print("xpath--------------------")
            print(xpath_)

            # xpath_ = '//*[@id="container"]/div/div[3]/div[1]/div/a[5]'
            # xpath_ = '//*[@id="container"]/div/div[3]/div[1]/div/a[4]'

            #12페이지 버튼
            # /html/body/div[1]/div[2]/div/div[3]/div[1]/div/a[4]
            
            driver.find_element(By.XPATH, xpath_).click()
            time.sleep(1)

f.close()