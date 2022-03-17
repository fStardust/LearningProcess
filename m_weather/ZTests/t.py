import json

import requests
import xmltodict

per_utl_str_location = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + "昆明"
per_response_location = requests.get(per_utl_str_location, verify=False).text
per_weather_dict_location = json.loads(json.dumps(xmltodict.parse(per_response_location)))
print(per_weather_dict_location)
per_com_loc = per_weather_dict_location["resp"]["zhishus"]["zhishu"]

n = ""
for i in per_com_loc:
    m = i['name'] + ':' + '\n' + i['detail'] + '\n'
    n = n + m


print(n)