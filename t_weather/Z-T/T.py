#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX
import json

import requests
import xmltodict



# 完整 万年历天气API -- T.xml
# 数据获取
def get_weather_data():
    city_name = "昆明"  # 位置自动获取 或 主动输入--web页面输入框   +
    url_w = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city_name  # 简单信息 -- 调整为城市代码 --T.xml +
    res = requests.get(url_w, verify=False)
    # html = etree.HTML(res_dict)
    res_text = res.text
    print(type(res_text))
    print(res_text)
    res_dict = xmltodict.parse(res_text)  # 将读取的xml字符串转换为字典
    json_str = json.dumps(res_dict, ensure_ascii=False)  # 将字典转换为json格式的字符串
    print(res_dict)

    weather_dict = res_dict['resp']
    item_dict1  = weather_dict['forecast']['weather']
    c = item_dict1['day']['type']
    print(c)

get_weather_data()
