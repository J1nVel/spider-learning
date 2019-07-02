# -*- coding:UTF-8 -*-
import requests
from bs4 import BeautifulSoup
# if __name__ == '__main__':
#   target = 'http://www.biqukan.com/1_1094/5403177.html'
#   req = requests.get(url = target)
#   # 网页编码是gbk
#   req.encoding = 'gb18030' 
#   bf = BeautifulSoup(req.text, 'html.parser')
#   # 在解析html之前，我们需要创建一个Beautiful Soup对象。BeautifulSoup函数里的参数就是我们已经获得的html信息
#   # 然后我们使用find_all方法，获得html信息中所有class属性为showtxt的div标签。find_all方法的第一个参数是获取的标签名，第二个参数class_是标签的属性
#   # 因为python中class是关键字，为了防止冲突，这里使用class_表示标签的class属性，class_后面跟着的showtxt就是属性值了
#   texts = bf.find_all('div', class_='showtxt')
#   print(texts[0].text.replace('\xa0'*8, '\n'))
if __name__ == '__main__':
  server = 'http://www.biqukan.com/'
  target = 'http://www.biqukan.com/1_1094/'
  req = requests.get(url = target)
  req.encoding = 'gb18030'
  titles_bf = BeautifulSoup(req.text, 'html.parser')
  titles = titles_bf.find_all('div', class_ = 'listmain')
  title = BeautifulSoup(str(titles[0])).find_all('a')
  for each in title:
    # each.string打印a标签里面的文字,get('href')获取a标签的href属性
    print(each.string, server + each.get('href'))