#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

from tools_my.crawls import Crawl
from bs4 import BeautifulSoup

class Course(Crawl):

    name = ''

    def get_courses(self,url):
        courses_list = []
        html =self.getText(url)
        soup = BeautifulSoup(html,'html.parser')
        cf = soup.find_all('ul',class_= 'cf')
        for ul in cf:
            try:
                li = ul.find_all('li')
                for i in li:
                    id = i.get('id')
                    name = i.find('h2').get_text()
                    # url = 'http://www.jikexueyuan.com/course/%s.html'%id
                    tup = (id,name)
                    courses_list.append(tup)
            except:
                print '获取 course 列表失败'
                continue
        return courses_list

    def get_num_classes(self,url):
        html = self.getText(url)
        soup = BeautifulSoup(html,'html.parser')
        try:
            box = soup.find('div',class_="lesson-box")
            ul = box.ul
            li = ul.find_all('li')
            num = li.__len__()
            return num
        except:
            print 'get the list of classes error'
            return 0