#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

from config import header
from tools_my.crawls import Crawl
from bs4 import BeautifulSoup
import requests
import os


class Down(Crawl):

    video_name = ''

    def get_url_class_down(self,url):
        try:
            # print url
            r = requests.get(url,headers=header)
            data = r.json()['data']
            down_url = data["urls"]
            name = data["title"]
            # print down_url
            tup = (name,down_url)
            return tup
        except:
            print 'get_url_down failed'
            return ''

    def get_url_resourse(self,url):
        try:
            r = requests.get(url)
            data = r.json()['data']
            # print data
            resourse_url = data['url']
            return resourse_url
        except:
            print 'get resourse url failed'
            return ''

    def down_file(self,url,dir,path):
        if not os.path.exists(path):  #如果文件存在就跳过
            r = self.getResponse(url)
            if os.path.exists(dir):   #判断要下载的目录是否存在
                with open(path,'wb') as f:
                    f.write(r.content)
            else:
                os.makedirs(dir)
                with open(path,'wb') as f:
                    f.write(r.content)


