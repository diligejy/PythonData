from bs4 import BeautifulSoup as bs
from pprint import pprint
import requests

html = requests.get('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EB%82%A0%EC%94%A8')
#pprint(html.text)

soup = bs(html.text, 'html.parser')
# pprint(soup)

data1 = soup.find('div', {'class' : 'detail_box'}) # 영역 추출
#pprint(data1)

data2 = data1.findAll('dd')
pprint(data2[0])