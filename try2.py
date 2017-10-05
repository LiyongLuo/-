import urllib2
response = urllib2.urlopen(https://baike.baidu.com/item/遗传病)
html = response.read()
print html
