import requests
from lxml import etree

city_name = '昆明'
url1 = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + city_name      # 详细信息 -- XML格式
res = requests.get(url1, verify=False)      # 获取成功 +
print(res.text)




