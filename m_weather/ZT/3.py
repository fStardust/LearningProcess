import json
import socket

import pandas as pd
import requests

city_file = "../static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)

def get_host_ip():
    """
    查询本机ip地址
    :return: ip
    """




def weather_data():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    user_ip = ip
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7&ip='+ user_ip + '&coor=bd09ll'
    response = requests.get(ip_api)
    city_dict = json.loads(response.text)
    print(city_dict)


weather_data()
