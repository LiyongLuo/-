# coding:utf-8
class UrlManager(object):
    def __init__(self):
        self.new_urls = set() # set,设置一个无序但不重复的元素集
        self.old_urls = set() # 将所有的连接分作两部分

    def has_new_url(self): #这个就是用来判断是否有待取的连接，但原理不知道
        return self.new_url_size() !=0

    def get_new_url(self):
        new_url = self.new_urls.pop() # 使用pop，是抽出，不是副本
        self.old_urls.add(new_url) #同时已爬取的应该增加
        return new_url

    def add_new_url(self,url): # 将解析出来的单个url，加入集合中
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
    def add_new_urls(self,urls): # 将解析出来的一堆URL，加入集合中，使用循环for
        if urls is  None or len(urls) ==0:
            return
        for url in urls:
            self.add_new_url(url)# 这里是调用上面的函数，不是直接加入
    def new_url_size(self):
        return len(self.new_urls)
    def old_url_size(self):
        return len(self.old_urls)
