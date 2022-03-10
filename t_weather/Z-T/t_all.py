import json

import requests
import xmltodict


# 数据获取
# 完整 万年历天气API -- T.xml
def get_weather_data():
    city_name = "昆明"  # 位置自动获取 或 主动输入--web页面输入框   +
    url_all_w = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city_name  # 完整信息 -- 调整为城市代码 --T.xml +
    res = requests.get(url_all_w, verify=False)
    all_res_dict = json.loads(json.dumps(xmltodict.parse(res.text)))  # 将 xml字符串转换为 dict 格式 -- 以便分析 +
    all_res_json = json.dumps(all_res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(all_res_dict)

    url_mini_w = 'http://wthrcdn.etouch.cn/weather_mini?city=' + city_name
    mini_res_dict = requests.get(url_mini_w).json()  # 获取数据 dict 格式 -- 以便分析 +
    mini_res_json = json.dumps(mini_res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(mini_res_dict)
    return all_res_dict, mini_res_dict


get_weather_data()
