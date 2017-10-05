# coding:utf-8
import re  # 导入正则表达式
import urlparse # 将url拆分，并且可以重组为url
from bs4 import BeautifulSoup # 网页解析

class HtmlParser(object):
    def parser(self,page_url,html_cont): # 由多个模块的时候一定要注意名称！！！
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'html.parser') #此处不能加编码，不然会冲突，并且报错，这里采用的是python标准库对内容进行解析，并获得html
        new_urls = self._get_new_urls(page_url, soup) #调用下面的方法，提取url
        new_data = self._get_new_data(page_url, soup)
        return new_urls, new_data

    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/wiki/.*')) # 抽取页面内所有带有wiki的连接
        for link in links:
            new_url = link['href'] #提取出相应的连接，但是原理不明
            new_full_url =urlparse.urljoin(page_url, new_url) # 将所提取的连接，同基连接结合，比如http://www.baidu.com/tieba,index 会返回http://www.baidu.com/index.but http://www.baidu.com/tieba/, index will return http://www.baidu.com/tieba/index
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self,page_url,soup):
        data = {}
        data['url'] =page_url # why use page_url,do not use full_url
        title = soup.find('h1', id="firstHeading")
        data['title'] = title.get_text()
        summary = soup.find('div', class_="mw-parser-output").find_all("p", limit=3)# 这里调用出来，是一个变量，而且是列表
        x = " "
        for i in summary:
            x = x + i.get_text()
        data['summary'] = x
        return data
