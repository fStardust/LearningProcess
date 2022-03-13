import json

import pandas as pd
import requests
from django.shortcuts import render

city_file = "./static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)


def weather_data(request):
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    response = requests.get(ip_api)
    city_dict = json.loads(response.text)
    print(city_dict)
    current_location = city_dict['content']['address_detail']['city']
    citycode = city_dict['content']['address_detail']['adcode']
    print(citycode)
    if request.method == 'POST':
        city = request.POST['city']
        for i in range(len(city_csv)):
            if city_csv['district'][i] == city:
                print(city_csv['district_geocode'][i])
                citycode = str(city_csv['district_geocode'][i])
        utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + citycode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    else:
        for i in range(len(city_csv)):
            if current_location == str(city_csv['city'][i]):
                citycode = str(city_csv['district_geocode'][i])
                break
        utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + citycode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'

    response = requests.get(utl_str)

    weather_dict = json.loads(response.text)
    print(weather_dict)
    res_json = json.dumps(weather_dict, ensure_ascii=False)
    data_dict = weather_dict['result']
    w_date = data_dict['forecasts']

    city = data_dict['location']['city']
    print('城市：{}'.format(city))

    nowtq = w_date[0]   # 改为 ***_weather
    onetq = w_date[1]
    twotq = w_date[2]
    threetq = w_date[3]
    fourtq = w_date[4]
    for item_dict1 in w_date:
        date = item_dict1['date']
        high = item_dict1['high']
        low = item_dict1['low']
        text_day = item_dict1['text_day']
        wd_day = item_dict1['wd_day']
        text_night = item_dict1['text_night']
        print(
            '时间：{}; 最高温度：{};最低温度：{}; 白天天气：{}; 白天风向：{}; 晚间天气：{}'.format(
                date, high, low, text_day, wd_day, text_night
            )
        )
    context = {
        'city': city,
        'weather_list': w_date,
        'nowtq': nowtq,
        'onetq': onetq,
        'twotq': twotq,
        'threetq': threetq,
        'fourtq': fourtq,
        'current_location': current_location,
    }

    return render(request, template_name='weather.html', context=context)
