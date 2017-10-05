#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re
import urlparse

r = requests.get("https://en.wikipedia.org/wiki/Genetic_disorder")
soup = BeautifulSoup(r.content, 'html.parser')
links = soup.find_all('a', href=re.compile(r'/wiki/.*'))
#for link in links:
#    new_url = link['href'] #提取出相应的连接，但是原理不明
#    new_full_url =urlparse.urljoin("https://en.wikipedia.org/", new_url)
#    print new_full_url
title = soup.find('h1', id="firstHeading")
print title.get_text()
summary = soup.find('div', class_="mw-parser-output").find_all('p',limit=3)
x = " "
for i in summary:
    x = x + i.get_text()
print x
