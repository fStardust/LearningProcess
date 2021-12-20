import requests
from django.http import HttpResponse

from weather.myKey import KEY

my_key = '&key=' + KEY

# 开发版实时天气 https://dev.qweather.com/docs/api/weather/weather-now/
url_api_weather = 'https://devapi.qweather.com/v7/weather/'
# 城市信息查询 支持文字，经纬度坐标(十进制，最多支持小数点后两位)
url_api_geo = 'https://geoapi.qweather.com/v2/city/'
# 开发版实时空气质量 https://dev.qweather.com/docs/api/air/air-now/
url_api_air = 'https://devapi.qweather.com/v7/air/now'


def get(api_type):
    url = url_api_weather + api_type + 'location=' + 'city_id' + my_key
    return requests.get(url).json()


# 页面显示内容
def index(request):
    city_id = '101010100'

    # if KEY == '':
    #     output = "No Key!"
    # else:
    #
    #     # o1 = city_id + '市'
    #     # o2 = '当前天气：' + get_now['now']['text'] + get_now['now']['temp'] + '°C'
    #     # o3 = '体感温度：' + get_now['now']['feelsLike'] + '°C'
    #     o4 = "Hello, world. You're at the weather index."
    #     output = get('now')
    # return HttpResponse(output)

    url = url_api_weather + 'now' + '?location=' + city_id + my_key
    return requests.get(url).json()


"""
    print(city_idname[3], str(city_idname[2]) + '市', str(city_idname[1]) + '区')     X
    print('当前天气：', get_now['now']['text'], get_now['now']['temp'], '°C', '体感温度', get_now['now']['feelsLike'], '°C')
    print('空气质量指数：', air_now['aqi'])
    print('降水可能性：', get_now['now']['humidity'], '%')
    print('今日天气：', daily()[0]['textDay'], daily()[0]['tempMin'], '-', daily()[0]['tempMax'], '°C')
"""