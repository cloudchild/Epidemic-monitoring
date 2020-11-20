import requests
import json
import pymysql
import time
import traceback


# 爬腾讯数据:
def get_data():
    """
    获取疫情数据
    :return: 历史数据
    """
    url = "https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5"
    headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"
    }
    res = requests.get(url,headers=headers)
    d = json.loads(res.text) # json.loads方法是将字符串转为字典
    data_all = json.loads(d["data"])
    areaTree_data = data_all["areaTree"]

    history = {}
    ds = data_all['lastUpdateTime']
    history[ds].update(data_all["chinaTotal"])# 历史数据 需要 累计确诊, 累计治愈,累计死亡, 现有确诊,无症状感染者,境外输入

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

# 存储数据
# 建立连接
conn = pymysql.connect(
    host="localhost",
    user="epi",
    password="123456",
    database = 'cov'
)  # 注意自己的用户名 与密码
# 创建游标
cursor = conn.cursor()
# 执行操作
sql=''
cursor.execute(sql)
conn.commit() # 提交事务 什么时候要要commit
# 获取查询结果
cursor.fetchall()
# 关闭连接
cursor.close()
conn.close()