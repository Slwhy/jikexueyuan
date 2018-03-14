#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

import requests

class Crawl(object):


    def getText(self,url):
        try:
            r = requests.get(url,timeout = 20)
            r.encoding = r.apparent_encoding
            print r.status_code,'request'
            self.html = r.text
            return r.text
        except:
            return 'request error'

    def getResponse(self, url):
        try:
            r = requests.get(url, timeout=20)
            r.encoding = r.apparent_encoding
            print r.status_code,'request'
            return r
        except:
            return 'request error'