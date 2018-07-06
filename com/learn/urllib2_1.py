#coding:utf8

import urllib2

#直接请求
response=urllib2.urlopen('http://fanyi.baidu.com/?aldtype=85#zh/en/%E7%88%AC%E8%99%AB')

#获取状态码，如果是200表示获取成功
print response.getcode()

#获取内容
cont=response.read()

print cont