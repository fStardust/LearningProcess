import json
import re

import requests
import xmltodict


# 完整 万年历天气API -- T.xml
# 数据获取
def get_weather_data():
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    response = requests.get(ip_api)
    city_dict = json.loads(response.text)
    city_name = city_dict['content']['address_detail']['city']
    url_w = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city_name  # 简单信息 -- 调整为城市代码 --T.xml +
    res = requests.get(url_w, verify=False)
    res_dict = json.loads(json.dumps(xmltodict.parse(res.text)))    # 将 xml字符串转换为 dict 格式 -- 以便分析 +
    res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_json)
    return res_dict


# 数据解析
def show_weather(res_dict):
    if res_dict.get('desc') == 'invilad-citykey':
        print("你输入的城市名有误，或者天气中心未收录你所在城市")
    elif res_dict.get('desc') == 'OK':
        forecast = res_dict.get('data').get('forecast')
        print('当前城市：', res_dict.get('data').get('city'))  # 默认从省-市-区- 尽可能详细 +
        print('实时温度：', res_dict.get('data').get('wendu') + '℃')
        print('感冒指数：', res_dict.get('data').get('ganmao'))
        print('天气概况：', forecast[0].get('type'))
        print('最高温度：', forecast[0].get('high'))
        print('最低温度：', forecast[0].get('low'))
        print('当前风向：', forecast[0].get('fengxiang'))
        wind_power = forecast[0].get('fengli')  # 有概率风力等级被XML-CDATA 包裹
        if 'CDATA' in wind_power:
            wind_power = re.split('[\[\]]', wind_power)[2]
        print('当前风级：', wind_power)

        four_day_forecast = 'N'  # 未来四天天气     web展示项！通知可选项-设置页可调整？    +
        condition = ['是', 'Y', 'y']
        if four_day_forecast in condition:
            print('--------未来几天天气--------')
            for i in range(1, 5):
                print('日期：', forecast[i].get('date'))
                print('风向：', forecast[i].get('fengxiang'))
                wind_power = forecast[i].get('fengli')  # 有概率风力等级被XML-CDATA 包裹
                if 'CDATA' in wind_power:
                    wind_power = re.split('[\[\]]', wind_power)[2]
                print('当前风级：', wind_power)
                print('高温：', forecast[i].get('high'))
                print('低温：', forecast[i].get('low'))
                print('天气：', forecast[i].get('type'))
                print('--------------------------')

    return 'OK'


get_weather_data()
show_weather(get_weather_data())
