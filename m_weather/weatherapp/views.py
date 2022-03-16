import json
import os

import pandas as pd
import requests
import xmltodict
from django.shortcuts import render

city_file = os.path.abspath('...//static/weather_district_id.csv')
city_csv = pd.read_csv(city_file)


# bai_utl_str:百度地图天气API;per_utl_str:万年历天气API
def weather_data(request):
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    bai_response = requests.get(ip_api)
    city_dict = json.loads(bai_response.text)
    current_location = city_dict['content']['address_detail']['city']
    if request.method == 'POST':
        city = request.POST['city']
        for i in range(len(city_csv)):
            if city == city_csv['district'][i]:
                districtcode = str(city_csv['districtcode'][i])
                citycode = str(city_csv['areacode'][i])
                break
        bai_utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + districtcode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
        per_utl_str = 'http://wthrcdn.etouch.cn/WeatherApi?citykey=' + citycode
    else:
        for i in range(len(city_csv)):
            if current_location == str(city_csv['city'][i]):
                districtcode = str(city_csv['districtcode'][i])
                citycode = str(city_csv['areacode'][i])
                break
        bai_utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + districtcode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
        per_utl_str = 'http://wthrcdn.etouch.cn/WeatherApi?citykey=' + citycode

    bai_response = requests.get(bai_utl_str).text
    per_response = requests.get(per_utl_str, verify=False).text

    print(bai_response)
    print(per_response)

    bai_weather_dict = json.loads(bai_response)
    per_weather_dict = json.loads(json.dumps(xmltodict.parse(per_response)))
    data_dict = bai_weather_dict['result']
    w_date = data_dict['forecasts']

    bai_weather_json = json.dumps(bai_weather_dict, ensure_ascii=False)
    per_weather_json = json.dumps(per_weather_dict, ensure_ascii=False)

    city = data_dict['location']['city']
    print('城市：{}'.format(city))

    per_recommend = per_weather_dict["resp"]["zhishus"]["zhishu"][0]["detail"]

    recommend = "天气舒适，建议穿着薄款，透气的衣物。推荐：长T、长裙、长裤等。"
    travel_recommend = per_recommend

    nowtq = w_date[0]  # 改为 ***_weather
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
        'recommend': recommend,
        'travel_recommend': travel_recommend,
    }

    return render(request, template_name='weather.html', context=context)

