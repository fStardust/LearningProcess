import json

import requests

print('____天气查询____')


# 数据获取
def get_weather_data():
    city_name = "昆明"
    url_w = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city_name  # 简单信息 -- json格式
    print(url_w)
    res_dict = requests.get(url_w).json()  # 获取数据 dict 格式 -- 以便分析 +
    res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_dict)
    return res_dict


# 数据解析
def show_weather(res_dict):
    if res_dict.get('desc') == 'invilad-citykey':
        print("你输入的城市名有误，或者天气中心未收录你所在城市")
    elif res_dict.get('desc') == 'OK':
        forecast = res_dict.get('data').get('forecast')

    return 'OK'


show_weather(get_weather_data())
