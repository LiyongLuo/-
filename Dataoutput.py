#coding: utf-8
import codecs
import csv


class DataOutput(object):
    def __init__(self):
        self.datas=[]
    def store_data(self, data):
        if data is None:
            return
        self.datas.append(data)

#    def output_html(self):
#        fout = codecs.open('wiki.html','w',encoding='utf-8')
#        fout.write("<html>")
#        fout.write("<head><meta charset='utf-8'/></head>'")
#        fout.write("<body>")
#        fout.write("<table>")
#        for data in self.datas:
#            fout.write("<tr>")
#            fout.write("<td>%r</td>"%data['url'])
#            fout.write("<td>%s</td>"%data['title'])
#            fout.write("<td>%s</td>"%data['summary'])
#            fout.write("</tr>")
#            self.datas.remove(data) #写完就删
#        fout.write("</table>")
#        fout.write("</body>")
#        fout.write("</html>")
#        fout.close()
    def output_csv(self):
        headers = ['url', 'title', 'summary']
        with open('wiki.csv', 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerow(headers)
            f_csv.writerow(self.datas)
            del self.datas
