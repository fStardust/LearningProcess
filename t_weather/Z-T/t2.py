import json
import re

import requests


location = '101010100'
key = 'd260678af4af47c8bba662fba49623f7'


# 数据获取
def get_weather_data():
    url_n = 'https://devapi.qweather.com/v7/weather/now?location=' + location + '&key=' + key  # 简单信息 -- 调整为城市代码
    res_dict = requests.get(url_n).json()  # 获取数据 dict 格式 -- 以便分析 +
    # res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_dict)
    print(type(res_dict))
    return res_dict


# 数据解析
def show_weather(res_dict):
    if res_dict['code'] != '200':
        print("当前数据未开放或当前位置不支持")
    else:
        data_now = res_dict.get('now')
        print(data_now)
        # q_data_web = res_dict.get('fxLink')
        # q_icon_code = data_now[0].get('icon')
        print('当前城市：', location)  # 默认从省-市-区- 尽可能详细 +
        print('实时温度：', data_now.get('temp') + '℃')
        print('体感温度：', data_now.get('feelsLike') + '℃')
        print('天气状况：', data_now.get('text'))
        print('主要风向：', data_now.get('windDir'))
        print('风力等级：', data_now.get('windScale') + '级')
        print('相对湿度：', data_now.get('humidity') + '%')
        if '雨' in data_now[0].get('text'):
            print('累计降水量：', data_now.get('precip') + 'mm')
    return 'ok'


get_weather_data()
show_weather(get_weather_data())
