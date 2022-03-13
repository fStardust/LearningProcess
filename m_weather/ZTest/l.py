import json

import pandas as pd
import requests

city_file = ".././static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)

ip = 'http://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7&ip=172.27.133.66&coor=bd09ll'
ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
response = requests.get(ip_api)
city_dict = json.loads(response.text)
res_json = json.dumps(city_dict, indent=4, ensure_ascii=False)
current_location = city_dict['content']['address_detail']['city']
citycode = city_dict['content']['address_detail']['adcode']


def location_judge():
    print("A")
    for i in range(len(city_csv)):
        # print(citycode)
        if citycode == str(city_csv['districtcode'][i]):
            print("y")
            province_name = city_csv['province'][i]
            print(city_csv['province'][i])
            print(province_name)
            city_name = str(city_csv['city'][i])
            print(city_name)
            district_name = str(city_csv['district'][i])
            location = province_name + city_name + district_name
            print(location)

