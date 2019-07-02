import requests
from bs4 import BeautifulSoup
class download(object):
  # 定义属性
  def __init__(self):
    self.sever = 'http://www.biqukan.com/'
    self.target = 'http://www.biqukan.com/1_1094/' # 目录地址
    self.title = [] # 存放章节名称
    self.urls = [] # 存放章节链接
    self.nums = 0 # 章节数

  # 获取章节链接
  def get_url(self):
    req = requests.get(url = self.target)
    # 解析dom结构,查找class为listmain的元素集合
    div = BeautifulSoup(req.text).find_all('div', class_ = 'listmain')
    # 查找集合中的a标签
    titles = BeautifulSoup(str(div[0])).find_all('a')
    self.nums = len(titles[4:-3])
    for each in titles[4:10]:
      self.title.append(each.string)
      self.urls.append(self.sever + each.get('href'))
  
  # 获取文章内容
  def get_content(self, target):
    req = requests.get(url = target)
    content = BeautifulSoup(req.text)
    texts = content.fond_all('div', class_ = 'showtxt')
    texts = texts[0].text.replace('\xa0'*8, '\n\n')
