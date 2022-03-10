from django.shortcuts import render

import requests

import json

def tq(request):
    ip_api = 'https://api.map.baidu.com/location/ip?ak=KHkVjtmfrM6NuzqxEALj0p8i1cUQot6Z'
    response = requests.get(ip_api)
    city_dict = json.loads(response.text)
    nowcity = city_dict['content']['address_detail']['city']
    if request.method == 'POST':
        city = request.POST['city']
        str = 'http://api.map.baidu.com/telematics/v3/weather?location=' + city + '&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'
    else:
        str = 'http://api.map.baidu.com/telematics/v3/weather?location=' + nowcity + '&output=json&ak=TueGDhCvwI6fOrQnLM0qmXxY9N0OkOiQ&callback=?'

    # city = input("请输入要查询的城市信息（例如：郑州，北京，上海）：")
    response = requests.get(str)

    json_str = response.text
    json_dict = json.loads(json_str)

    data_dict = json_dict['results']
    lin = data_dict[0]
    index = lin['index']
    w_date = lin['weather_data']

    city = data_dict[0]['currentCity']
    pm = data_dict[0]['pm25']
    print('城市：{}; pm25：{};'.format(city, pm))

    nowtq = w_date[0]
    onetq = w_date[1]
    twotq = w_date[2]
    threetq = w_date[3]
    for item_dict1 in w_date:
        date = item_dict1['date']
        temperature = item_dict1['temperature']
        weather = item_dict1['weather']
        wind = item_dict1['wind']
        print('时间：{}; 温度：{}; 天气：{}; 风向：{}'.format(date, temperature, weather, wind))
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