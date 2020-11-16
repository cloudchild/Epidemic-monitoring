# 使用 requests
# import requests
#
# url = "http://www.douban.com"
#
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
# }
#
# r = requests.get(url,headers=headers)

# print(r.headers) #获取响应头
# print(r.status_code) # 获取状态码
# print(r.url)
# print(r.encoding) # 查看编码
# r.encoding = "UTF-8"
# html = r.text # 获取内容
# print(html)
# 使用urllib3
# from urllib import request
#
# url = "http://www.douban.com"
# # 添加headers反爬措施
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
# }
# req = request.Request(url,headers=headers)
# res = request.urlopen(req)
# html = res.read()
# html.decode("utf-8")
# print(res.info())     # 响应头
# print(res.getcode()) # 返回状态码 2xx 正常，
# print(res.geturl()) # 返回响应地址

from bs4 import BeautifulSoup
import re
from lxml import etree
# 爬四川卫健委
# import requests
# url = "http://wsjkw.sc.gov.cn/scwsjkw/gzbd/fyzt.shtml"
# res = requests.get(url)
# res.encoding = 'UTF-8'
# html = res.text
# soup = BeautifulSoup(html,"lxml")
# t = soup.find("h2").text
# a = soup.find("a")
# # print(t,a.attrs["href"])
# url_new = "http://wsjkw.sc.gov.cn" + a.attrs["href"]
# # print(url_new)  #获取新地址
#
# res = requests.get(url_new)
# res.encoding = "utf-8"
# html = res.text
# soup = BeautifulSoup(html,"lxml")
# # d = soup.find(class_="wy_contMain fontSt")
# # p =d.find("p")
# p = soup.find_all("p",limit=2)[1] # 从列表中获取第二个元素，limit 获取标签个数
# text = p.text
# # print(text)
# # patten = "新型冠状病毒肺炎确诊病例(\d+)"
# patten = "新型冠状病毒肺炎确诊病例(\d+).*?境外输入(\d+)例.*?治愈出院(\d+)例.*?死亡(\d+)例"
# res = re.search(patten,text)
# print(res.groups())
# print(res.group(0))
# print(res.group(1),res.group(2),res.group(3),res.group(4))

# 爬腾讯
