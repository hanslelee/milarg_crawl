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
from selenium.webdriver.support.ui import Select


import urllib3
urllib3.disable_warnings()

# pageLimit = 6000
pageLimit = 6212
articleNumPerPage = 100

f = open('./mil_news_data_tongil.txt', 'w')

res = requests.get(f"https://nkinfo.unikorea.go.kr/nkp/news/list.do", verify=False)
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://nkinfo.unikorea.go.kr/nkp/news/list.do")
htmlCode = res.text
soup = BeautifulSoup(htmlCode, 'html.parser')


select = Select(driver.find_element(By.XPATH, '//*[@id="edcuation_selectDataLength"]'))
select.select_by_value('100')
driver.implicitly_wait(3)

xpath_ = f'//*[@id="contents"]/div[2]/ul/li[13]'
driver.find_element(By.XPATH, xpath_).click()
time.sleep(2)
page_source = driver.page_source


for pageNum in range(1, pageLimit+1): # 1에서 100까지 10씩 증가 (1, 11, 21, ..., 91)
    print('pageNum : '+str(pageNum))

    for articleNum in range(1, articleNumPerPage+1):
        if (articleNum-1)%100 == 0:
            if pageNum%10 == 0:
                xpath_ = f'//*[@id="contents"]/div[2]/ul/li[13]' #3    
            else :
                xpath_ = f'//*[@id="contents"]/div[2]/ul/li[{pageNum%10 + 3}]' #3    
                
                # //*[@id="contents"]/div[2]/ul/li[4]
            
            

            driver.find_element(By.XPATH, xpath_).click()
            time.sleep(2)
            
        
            page_source = driver.page_source

        # BeautifulSoup을 사용하여 HTML 파싱
        soup = BeautifulSoup(page_source, 'html.parser')
        selectElement = f'#contents > div.table > table > tbody > tr:nth-child({articleNum}) > td.ta_left > a'
        

        titleList = soup.select(selectElement)
        print(titleList)

        for title in titleList:
            articleTitle = eraseSpace(title.text)
            f.write('국방\t' + articleTitle + '\n')
            print(articleTitle)


f.close()