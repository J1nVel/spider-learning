'''
python抓取电影天堂最新电影迅雷下载地址链接信息
'''
import requests,sys
from bs4 import BeautifulSoup

# 定义解析函数
def bs_fn(content, html_label, class_name):
  bf = BeautifulSoup(content, 'html.parser').find_all(html_label, class_ = class_name)
  return bf

# 定义写入文件函数
def writer(path, text):
  with open(path, 'a', encoding = "utf-8") as f:
    # f.write(name + '\n')
    f.writelines(text)
    f.write('\n\n')

# 对单个电影页面的链接进行爬取
def single_magnet(url):
  single_html = requests.get(url)
  single_html.encoding = 'gb2312'
  zoom = BeautifulSoup(single_html.text, 'html.parser').find_all(id = 'Zoom')
  magnet = bs_fn(str(zoom), 'a', '')[0].get('href')
  return magnet

if __name__ == '__main__':
  html = requests.get(url = 'https://www.dytt8.net/')
  html.encoding = 'gb2312'
  html_text = bs_fn(html.text, 'div', 'bd3rl')[0]
  list_col = bs_fn(str(html_text), 'div', 'co_content8')
  # list_title = []
  for i in range(len(list_col)):
    # link = []
    a_link = bs_fn(str(list_col[i]), 'a', '')
    for j in range(len(a_link)):
      if a_link[j].get('href') != '/app.html' and a_link[j].get('href') != '/html/gndy/dyzz/index.html' and a_link[j].get('href') != '/html/gndy/index.html':
        magnet = 'https://www.dytt8.net' + a_link[j].get('href')
        writer('电影磁力链接.txt', a_link[j].text + '\n' + single_magnet(magnet))
