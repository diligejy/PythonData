import requests
from bs4 import BeautifulSoup

url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&amp;theatercode=0056&amp;date=20190812'
html = requests.get(url)
print(html.text)