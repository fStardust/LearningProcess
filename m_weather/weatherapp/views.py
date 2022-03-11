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
    nowcity = city_dict['content']['address_detail']['city']
    citycode = city_dict['content']['address_detail']['adcode']
    if request.method == 'POST':
        city = request.POST['city']
        for i in range(len(city_csv)):
            if city_csv['district'][i] == city:
                print(city_csv['district_geocode'][i])
                citycode = str(city_csv['district_geocode'][i])
        utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + citycode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    else:
        utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + citycode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'

    response = requests.get(utl_str)

    json_str = response.text
    json_dict = json.loads(json_str)
    data_dict = json_dict['result']
    w_date = data_dict['forecasts']

    city = data_dict['location']['city']
    print('城市：{}; pm25：{};'.format(city, "56"))

    nowtq = w_date[0]
    onetq = w_date[1]
    twotq = w_date[2]
    threetq = w_date[3]
    for item_dict1 in w_date:
        date = item_dict1['date']
        high = item_dict1['high']
        text_day = item_dict1['text_day']
        wd_day = item_dict1['wd_day']
        print('时间：{}; 最高温度：{}; 白天天气：{}; 白天风向：{}'.format(date, high, text_day, wd_day))
    context = {
        'city': city,
        'weather_list': w_date,
        'nowtq': nowtq,
        'onetq': onetq,
        'twotq': twotq,
        'threetq': threetq,
        'nowcity': nowcity,
    }

    return render(request, template_name='weather.html', context=context)
