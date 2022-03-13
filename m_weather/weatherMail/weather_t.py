import json

import pandas as pd
import requests
import xmltodict

city_file = "./static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)


# Create your views here.

def weather_data():
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    response = requests.get(ip_api)
    city_dict = json.loads(response.text)
    nowcity = city_dict['content']['address_detail']['city']
    utl_str = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + nowcity  # 简单信息使用城市代码 --T.xml +
    res_text = requests.get(utl_str, verify=False).text  # 获取数据mxl text 格式
    res_dict = json.loads(json.dumps(xmltodict.parse(res_text)))  # 数据mxl Dict 格式 -- 以便分析 +
    # res_json = json.dumps(res_dict, ensure_ascii=False)  # 数据  json 标准化 -- 以便存储
    print(res_dict)

    # 获取API城市名 -- 需要两个 -- 现在即时搜索
    weather_dict = res_dict['resp']
    if weather_dict['city'] not in weather_dict:
        print("你输入的城市名有误，或者天气中心未收录你所在城市")
    else:
        city = weather_dict['city']

    print('城市：{}; pm25：{};'.format(city, "56"))

    w_date = weather_dict['forecast']['weather']

    nowtq = w_date[0]
    onetq = w_date[1]
    twotq = w_date[2]
    threetq = w_date[3]
    for item_dict1 in w_date:
        date = item_dict1['date']
        high = item_dict1['high']
        type = item_dict1['day']['type']
        fengxiang = item_dict1['day']['fengxiang']
        print('时间：{}; 最高温度：{}; 白天天气：{}; 白天风向：{}'.format(date, high, type, fengxiang))
