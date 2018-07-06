#coding:utf8

import urllib2,cookielib
from com.learn.urllib2_1 import response

#创建cookie容器
cj=cookielib.CookieJar()

#创建1个opener
opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))

#创建urllib2安装opener
urllib2.install_opener(opener)

#使用带有cookie的urllib2访问网页
response=urllib2.urlopen('https://www.baidu.com')
