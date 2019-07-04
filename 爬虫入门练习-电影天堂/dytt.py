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

if __name__ == '__main__':
  html = requests.get(url = 'https://www.dytt8.net/')
  html.encoding = 'gb2312'
  html_text = bs_fn(html.text, 'div', 'bd3rl')
  list_col = bs_fn(html_text, 'div', 'co_area2')
  print(list_col[0])