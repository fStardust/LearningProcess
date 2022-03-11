import json

import requests

ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
response = requests.get(ip_api)
city_dict = json.loads(response.text)
nowcity = city_dict['content']['address_detail']['city']

print(nowcity)