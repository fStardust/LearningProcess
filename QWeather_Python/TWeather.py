import requests
import time
import json
from myKey import KEY

''' official website  https://www.qweather.com '''
'''      dev website  https://dev.qweather.com'''
mykey = '&key=' + KEY

# 开发版实时天气 https://dev.qweather.com/docs/api/weather/weather-now/
url_api_weather = 'https://devapi.qweather.com/v7/weather/'
# 城市信息查询 支持文字，经纬度坐标(十进制，最多支持小数点后两位)
url_api_geo = 'https://geoapi.qweather.com/v2/city/'
# 开发版实时空气质量 https://dev.qweather.com/docs/api/air/air-now/
url_api_air = 'https://devapi.qweather.com/v7/air/now'


def get(api_type):
    url = url_api_weather + api_type + '?location=' + city_id + mykey
    return requests.get(url).json()


def air(city_id):
    url = url_api_air + '?location=' + city_id + mykey
    return requests.get(url).json()


def get_city(city_kw):
    url_v2 = url_api_geo + 'lookup?location=' + city_kw + mykey
    city = requests.get(url_v2).json()['location'][0]

    city_id = city['id']
    district_name = city['name']
    city_name = city['adm2']
    province_name = city['adm1']
    country_name = city['country']
    lat = city['lat']
    lon = city['lon']

    return city_id, district_name, city_name, province_name, country_name, lat, lon


def tWeather():

    def get(api_type):
        url = url_api_weather + api_type + '?location=' + city_id + mykey
        return requests.get(url).json()

    city_idname = get_city('北京')

    city_id = city_idname[0]

    get_now = get('now')
    return get_now, '\n', city_id

print(tWeather())

