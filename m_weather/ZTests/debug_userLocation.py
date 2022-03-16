import json

import pandas as pd
import requests

city_file = "../static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)
ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
response = requests.get(ip_api)
city_dict = json.loads(response.text)
res_json = json.dumps(city_dict, indent=4, ensure_ascii=False)
current_location = city_dict['content']['address_detail']['city']
citycode = city_dict['content']['address_detail']['adcode']


# 获得城市（区县）对应城市代码（citycode）
def location_judge():
    for i in range(len(city_csv)):
        if citycode == str(city_csv['districtcode'][i]):
            province_name = city_csv['province'][i]
            city_name = str(city_csv['city'][i])
            district_name = str(city_csv['district'][i])
            location = province_name + city_name + district_name
            print(location)


print("**********百度通过IP获取定位API测试**********")
print("测试结果--测试地点：云南师范大学商学院海源校区·位于云南省昆明市五华区")
print("-----------------------------------------")
print("1.接口返回Json信息如下（经过数据格式化处理分行输出）:")
print(res_json)
print("2.接口返回IP所属区县代码：")
print(citycode)
print("3.当前返回区县代码所属 省·市·区县 名(通过解析百度官方城市代码对照csv文件---weather_district_id.csv)：")
location_judge()

print("4.调整后返回区县代码(默认为市级行政中心)：")
for i in range(len(city_csv)):
    if current_location == str(city_csv['city'][i]):
        citycode = str(city_csv['district_geocode'][i])
        print(citycode)
        break
print("5.调整后区县代码所属地 省·市·区县(通过解析百度官方城市代码对照csv文件---weather_district_id.csv)：")
location_judge()
