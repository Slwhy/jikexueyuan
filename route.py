#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

from tools_my.crawls import Crawl
from bs4 import BeautifulSoup

class Route(Crawl):

    def get_routes(self,url):
        routes_list = []
        html = self.getText(url)
        soup = BeautifulSoup(html, 'html.parser')
        pathlist = soup.find('div', class_='pathlist').div
        print '正在采集学习路线...............'
        count = 1
        for i in pathlist:
            try:
                sys_tup = ("http:" + i.get('href'), i.img.get('alt'))  # (url,name)
                print str(count)+'\t',sys_tup[0] + '\t', sys_tup[1] + '\n'
                routes_list.append(sys_tup)
                count = count + 1
            except AttributeError:
                continue

        print '共采集到 %s 条学习路线'% routes_list.__len__()
        return routes_list

    def select(self):
        n = raw_input("\n请输入你想爬取的学习路线编号（如果想按序全部爬取请输入0）：\n")
        return int(n)

