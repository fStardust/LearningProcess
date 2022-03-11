import json
import re

import requests
import xmltodict


# 完整 万年历天气API -- T.xml
# 数据获取
def get_weather_data():
    city_name = "昆明"  # 位置自动获取 或 主动输入--web页面输入框   +
    url_w = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city_name  # 简单信息 -- 调整为城市代码 --T.xml +
    res = requests.get(url_w, verify=False)
    res_dict = json.loads(json.dumps(xmltodict.parse(res.text)))    # 将 xml字符串转换为 dict 格式 -- 以便分析 +
    res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_dict)
    return res_dict





get_weather_data()
show_weather(get_weather_data())
