# 使用 requests
# import requests
# url = "http://www.douban.com"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
# }
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
# import requests
# import json
# url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5" #
# headers = {
# "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
# }
# res = requests.get(url,headers=headers)
# # print(res.text)
# d = json.loads(res.text) # json.loads方法是将字符串转为字典
# print(d)
# print(d.keys()) #查看数据的键值 ret是响应值，0代表请求成功，data里是我们需要的数据
# print(d["data"])
# print(d["data"].keys()) # 需要对data中的数据进行解析,查看键值
# data_all = json.loads(d['data']) # d["data"]是字符串，通过json.loads转字典
# print(data_all.keys())
# lastUpdateTime是最新更新时间，chinaTotal是全国疫情总数，chinaAdd是全国新增数据，
# isShowAdd代表是否展示新增数据，showAddSwitch是显示哪些数据，areaTree中有全国疫情数据
# print(data_all['lastUpdateTime'])
# print(data_all['chinaTotal']) # 全国累计
# print(data_all['chinaAdd']) # 全国新增
# print(data_all['isShowAdd'])
# print(data_all['showAddSwitch'])
# print(data_all['areaTree'])
# print(len(data_all['areaTree'])) #只有一个数据,
# print(data_all['areaTree'][0]) # 查看这个数据为字典
# print(data_all['areaTree'][0].keys()) # 查看字典键值
# areaTree_data = data_all["areaTree"]
# print(areaTree_data[0]['name'])
# print(areaTree_data[0]['today'])
# print(areaTree_data[0]['total'])
# print(areaTree_data[0]['children'])
# print(len(areaTree_data[0]['children'])) # 列表,查看长度,
# history = {} # 历史数据
# for pro_infos in areaTree_data[0]["children"]: # 遍历列表数据,列表数据为每个省份的信息
#     province_name = pro_infos['name']  # 省名
#     # print(pro_infos.keys())
#     for city_infos in pro_infos['children']:
#         # print(city_infos.keys())
#         city_name = city_infos['name']
#         confirm = city_infos['total']['confirm']  # 历史总数
#         confirm_add = city_infos['today']['confirm']  # 今日增加数
#         heal = city_infos['total']['heal']  # 治愈
#         dead = city_infos['total']['dead']  # 死亡
#         print(province_name, city_name, confirm, confirm_add, heal, dead)

# 爬腾讯数据:
import requests
import json
def get_data():
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    res = requests.get(url,headers=headers)
    d = json.loads(res.text) # json.loads方法是将字符串转为字典
    data_all = json.loads(d["data"])
    areaTree_data = data_all["areaTree"]
    history = data_all["chinaTotal"]# 历史数据 需要 累计确诊, 累计治愈,累计死亡, 现有确诊,无症状感染者,境外输入

    details = [] # 当天详细数据
    update_time = data_all['lastUpdateTime']
    data_province = areaTree_data[0]["children"]
    for pro_infos in data_province: # 遍历列表数据,列表数据为每个省份的信息
        province_name = pro_infos['name']  # 省名
        # print(pro_infos.keys())
        for city_infos in pro_infos['children']:
            # print(city_infos.keys())
            city_name = city_infos['name']
            confirm = city_infos['total']['confirm']  # 历史总数
            confirm_add = city_infos['today']['confirm']  # 今日增加数
            heal = city_infos['total']['heal']  # 治愈
            dead = city_infos['total']['dead']  # 死亡
            details.append([update_time,province_name, city_name, confirm, confirm_add, heal, dead])
    return history,details