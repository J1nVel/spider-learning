import requests, sys
from bs4 import BeautifulSoup
# 定义类
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
    # 小说网页的编码为gbk，代码编码为utf-8，故需要修改
    req.encoding = 'gb18030'
    # 解析dom结构,查找class为listmain的元素集合
    div = BeautifulSoup(req.text, 'html.parser').find_all('div', class_ = 'listmain')
    # 集合的第一项为所需元素，转为字符串后由beautifsoup解析，再查找集合中的a标签
    titles = BeautifulSoup(str(div[0]), 'html.parser').find_all('a')
    # titles集合的长度为章节链接的长度,倒序？？？
    self.nums = len(titles[0:5])
    # 对titles进行循环，一个each为一个a标签元素，string为文字，self.sever+each.get('href')为链接
    for each in titles[0:5]:
      self.title.append(each.string)
      self.urls.append(self.sever + each.get('href'))
    # i = self.nums - 1
    # while i >= 0:
    #   self.title.append(titles[i].string)
    #   self.urls.append(self.sever + titles[i].get('href'))
    #   i = i - 1
  
  # 获取文章内容
  # 传入需要获取的链接
  def get_content(self, target):
    req = requests.get(url = target)
    req.encoding = 'gb18030'
    content = BeautifulSoup(req.text, 'html.parser')
    texts = content.find_all('div', class_ = 'showtxt')
    # 把空格换位换行符
    texts = texts[0].text.replace('\xa0'*8, '\n\n')
    return texts
  
  # 将爬取的文章写入文件
  def writer(self, name, path, text):
  	'''
    文件写入函数 path表示文件名
    'a'：打开一个文件用于追加。如果该文件已存在，文件指针将会放在文件的结尾。
    也就是说，新的内容将会被写入到已有内容之后。如果该文件不存在，创建新文件进行写入。
    '''
  	with open(path, 'a', encoding = 'utf-8') as f:
      # write() 方法用于向文件中写入指定字符串  writelines() 方法用于向文件中写入一序列的字符串
  		f.write(name + '\n')
  		f.writelines(text)
  		f.write('\n')


# 调用函数
'''
一个python的文件有两种使用的方法，第一是直接作为脚本执行，第二是import到其他的python脚本中被调用（模块重用）执行。
因此if __name__ == 'main': 的作用就是控制这两种情况执行代码的过程，
在if __name__ == 'main': 下的代码只有在第一种情况下（即文件作为脚本直接执行）才会被执行，而import到其他脚本中是不会被执行的
'''
if __name__ == '__main__':
	# 参数？？
  dl = download()
  dl.get_url()
  print('《一年永恒》开始下载：')
  # for i in range(dl.nums):
  #   dl.writer(dl.title[i], '一念永恒.txt', dl.get_content(dl.urls[i]))
  i = dl.nums - 1
  while i >= 0:
    dl.writer(dl.title[i], '一念永恒.txt', dl.get_content(dl.urls[i]))
    i = i - 1
    # %.2f%%: %.2f表示输出格式，保留两位小数，%%表示输出百分号
    # '\r' 回车，回到当前行的行首，而不会换到下一行，如果接着输出的话，本行以前的内容会被逐一覆盖
    # '\n' 换行，换到当前位置的下一行
    sys.stdout.write("已下载:%.2f%%" % float((dl.nums - 1 - i)/dl.nums*100) + '\r')
    sys.stdout.flush()
    '''
    flush() 方法是用来刷新缓冲区的，即将缓冲区中的数据立刻写入文件，
    同时清空缓冲区，不需要是被动的等待输出缓冲区写入
    '''
  print('《一年永恒》下载完成')