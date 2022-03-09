import gzip
import json
import urllib.request
import requests
from lxml import html

print('____天气查询____')


def get_weather_data():
    city_name = "昆明"
    url1 = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city_name      # 简单信息 -- json格式
    print(url1)
    res = requests.get(url1)
    res_dict = requests.get(url1).json()        # 获取数据 dict 格式 -- 以便分析 +
    print(res_dict)
    res_json = json.dumps(res_dict, ensure_ascii=False)    # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_json)


get_weather_data()


