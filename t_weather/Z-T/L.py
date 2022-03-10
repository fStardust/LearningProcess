import requests

location = 'kunming'
key = 'd260678af4af47c8bba662fba49623f7'


def get_location_data():
    url_n = 'https://geoapi.qweather.com/v2/city/lookup?location=' + location + '&key=' + key  # 简单信息 -- 调整为城市代码
    res_dict = requests.get(url_n).json()  # 获取数据 dict 格式 -- 以便分析 +
    # res_json = json.dumps(res_dict, ensure_ascii=False)  # 获取数据 进行 json 标准化 -- 以便存储 +
    print(res_dict)
    print(type(res_dict))
    return res_dict


get_location_data()
