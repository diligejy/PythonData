# 2019년 8월기준 네이버 우회
from selenium import webdriver
from bs4 import BeautifulSoup as bs

import time
import os, sys

# pyInstaller를 설치하면 pyInstaller가 시스템 함수 내부에 frozen 변수설치 
# 크롬드라이버가 번들되어있는 exe파일 내부에 번들되어있는 상태인지
# 컴퓨터 내부에서 직접 실행하기 위해 파일이 존재하는 것인지 확인
if getattr(sys, 'frozen', False):
    chromedriver_path = os.path.join(sys._MEIPASS, 'chromedriver.exe')
    driver = webdriver.Chrome(chromedriver_path)
else:
    driver = webdriver.Chrome()    

driver = webdriver.Chrome()

driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

## 네이버 로그인 우회 
 
id = ""
pw = ""
 
# execute_script 함수 사용 (자바스크립트로 아이디, 패스워드를 넘겨주는 형태)
driver.execute_script("document.getElementsByName('id')[0].value=\'"+id+"\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'"+pw+"\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

time.sleep(2)

base_url = 'https://cafe.naver.com/pnmath'
url = '/ArticleList.nhn?search.clubid=23380319&amp;search.menuid=311&amp;search.boardtype=L'

driver.get(base_url + url)
driver.switch_to.frame('cafe_main') # iframe 내부로 접근

soup = bs(driver.page_source, 'html.parser')
soup = soup.find_all(class_ = 'article-board m-tcol-c')[1]
rows = soup.find_all('td', class_ = 'td_article')

for row in rows:
    article_title = row.find('a', class_ = 'article')
    if len(article_title.find_all('span'))> 0:
        for s in soup('span'):
            s.extract()
    article_title = article_title.get_text().strip()
    print(article_title)

driver.close()