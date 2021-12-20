import requests
import time
from weather.myKey import KEY

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


def now():
    return get_now['now']


def daily():
    return get_daily['daily']


def hourly():
    return get_hourly['hourly']


if __name__ == '__main__':
    if KEY == '':
        print('No Key! Get it first!')

    print('请输入城市:')
    city_input = input()
    city_idname = get_city(city_input)

    city_id = city_idname[0]

    get_now = get('now')
    get_daily = get('3d')  # 3d/7d/10d/15d
    get_hourly = get('24h')  # 24h/72h/168h
    air_now = air(city_id)['now']

    # print(json.dumps(get_now, sort_keys=True, indent=4))
    if city_idname[2] == city_idname[1]:
        print(city_idname[3], str(city_idname[2]) + '市')
    else:
        print(city_idname[3], str(city_idname[2]) + '市', str(city_idname[1]) + '区')
    print('当前天气：', get_now['now']['text'], get_now['now']['temp'], '°C', '体感温度', get_now['now']['feelsLike'], '°C')
    print('空气质量指数：', air_now['aqi'])
    print('降水可能性：', get_now['now']['humidity'], '%')
    print('今日天气：', daily()[0]['textDay'], daily()[0]['tempMin'], '-', daily()[0]['tempMax'], '°C')

    # nHoursLater = 1  # future weather hourly
    # print(nHoursLater, '小时后天气：', hourly()[1]['text'], hourly()[1]['temp'], '°C')

    nDaysLater = 1  # future weather daily
    print(nDaysLater, '天后天气：', daily()[nDaysLater]['textDay'], daily()[nDaysLater]['tempMin'], '-',
          daily()[nDaysLater]['tempMax'], '°C')

today = daily()[0]
tomorrow = daily()[1]

# 可以在服务器上运行的一点小设想
while True:
    if time.asctime()[11:13] == '17':

        # 明天如果有雨晚上十点告诉我
        for rain in tomorrow['textDay']:
            if rain == '雨':
                print('明天有雨，通过邮件或啥的告诉我')
                break  # 防止明天是 '暴雨到大暴雨' 两个雨字的天气
            else:  # else 其实没啥意义 ， 而且会执行多次
                print('什么也不干，继续循环')

        # 明天与今天温差过大提醒
        if int(tomorrow['tempMax']) - int(today['tempMax']) > 5:
            print('明天很热，通过邮件或啥的告诉我')
        if int(today['tempMin']) - int(tomorrow['tempMin']) > 5:
            print('明天很冷，通过邮件或啥的告诉我')

    time.sleep(1000)
