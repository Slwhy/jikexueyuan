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
        for i in pathlist:
            try:
                sys_tup = ("http:" + i.get('href'), i.img.get('alt'))  # (url,name)
                print sys_tup[0] + '\t', sys_tup[1] + '\n'
                routes_list.append(sys_tup)
            except AttributeError:
                continue

        print '共采集到 %s 条学习路线'% routes_list.__len__()
        return routes_list

