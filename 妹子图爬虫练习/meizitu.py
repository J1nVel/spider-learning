'''
每页24个主题写真，
每个主题下有几十张照片，每张照片一个网页.
网页结构简单.用 BeautifulSoup 就可以轻松爬取。
网站140+页.  每页的网址很有规律 1-140
只要能获得一个页面里面的数据
剩下页面的数据只要从1到140 循环.就可以了
http://www.mzitu.com/page/1
http://www.mzitu.com/page/2
http://www.mzitu.com/page/3
......
http://www.mzitu.com/page/140

每页24个主题. 每个主题一个链接.
http://www.mzitu.com/87933
http://www.mzitu.com/87825
每个主题之间就没什么联系了.
所有主题的网址就得手动爬下来.

每个主题诺干张图片. 每张图片一个网址
http://www.mzitu.com/86819/1
http://www.mzitu.com/86819/2
http://www.mzitu.com/86819/3
单个主题下的图片很有规律
只要知道这个主题的图片数量就能循环出某主题下所有的网址.
这个网址 不等于 图片的网址.
图片网址 需要到每个网页下面匹配出来.

爬虫步骤：
整个妹子图所有主题的网址.            get_page1_urls
某主题下第一张照片地址               get_img_url
某主题的照片数                       get_page_num
用循环获取某主题下所有照片地址       get_img_url
获取各个主题的主题名字               get_img_title
下载所有主题下的所有照片             download_imgs
'''
# 0: 依赖模块
import urllib.request         # 获取网页内容
from bs4 import BeautifulSoup # 解析网页内容
import re                     # 正则表达式模块
import os                     # 系统路径模块: 创建文件夹用
import socket                 # 下载用到?
import time                   # 下载用到?
