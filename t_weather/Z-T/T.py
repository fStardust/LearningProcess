import json

import requests


# 数据获取
def get_weather_data():
    # key = 'fd034bf8fe70289698ec4ea79876feree'
    url_w = 'http://api.weatherdt.com/common/?area=101010100&type=index&key=fd034bf8fe70289698ec4ea79876feree'  # 简单信息 -- 调整为城市代码
    res_dict = requests.get(url_w).json()  # 获取数据 dict 格式 -- 以便分析 +
    # res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_dict)


get_weather_data()
