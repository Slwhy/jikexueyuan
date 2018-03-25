#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

import os
basedir = os.path.abspath(os.path.dirname(__file__))
# print basedir

video_path = u'/home/acs/视频'

class MysqlConfig:
    user = 'root'
    pwd = ''
    db = 'jikexuey'



header = {

    'Accept':'*/*',
    'Accept-Encoding':'gzip, deflate',
    'Accept-Language':'zh-CN,zh;q=0.9',
    'Cache-Control':'no-cache',
    'Connection':'keep-alive',
    'Pragma':'no-cache',
    'Referer':'http://www.jikexueyuan.com/path/',
    'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.108 Safari/537.36'

}