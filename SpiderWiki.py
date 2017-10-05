#coding:utf-8
from Dataoutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from URLManager import UrlManager

class SpiderWiki(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        while(self.manager.has_new_url() and self.manager.old_url_size()<100):
            try:
                new_url = self.manager.get_new_url()
                html = self.downloader.download(new_url)
                new_urls, data = self.parser.parser(new_url, html)
                self.manager.add_new_urls(new_urls)
                self.output.store_data(data)
                print "已经抓取%s个链接"%self.manager.old_url_size()
            except Exception, e:
                print "crawl failed"
        self.output.output_csv()

if __name__=="__main__":
    spider_wiki = SpiderWiki()
    spider_wiki.crawl("https://en.wikipedia.org/wiki/Genetic_disorder")
