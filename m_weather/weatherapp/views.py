import json
import os
from datetime import datetime

import pandas as pd
import requests
import xmltodict
from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render
from django_apscheduler.jobstores import DjangoJobStore, register_job

from weatherMail.communication import com_weather
from weatherapp.models import TrigTime, LogSheet

city_file = os.path.abspath('.\information\weather_district_id.csv')
city_csv = pd.read_csv(city_file)

# log_sheet = LogSheet.objects.all()

trig_time = TrigTime.objects.last()
test_id = "timer" + str(trig_time.id)
timer_hour = trig_time.trig_time_hour
timer_min = trig_time.trig_time_min
the_daily_time = timer_hour + ":" + timer_min

# 定时触发
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, 'cron', day_of_week='*', hour=timer_hour, minute=timer_min, id=test_id)
def com_timer():
    localtime = datetime.now()
    print(localtime.strftime("%Y-%m-%d %H:%M:%S"))
    log_sheet = LogSheet(run_time=localtime, choice_text="text")
    log_sheet.save()
    com_weather()


scheduler.start()  # 开始执行调度器
# if request.method == 'POST':
#     scheduler.modify_job(scheduler, hour=timer_hour, minute=timer_min)


# 修改定时提醒时间
def change_time(request):
    daily_time_bef = the_daily_time
    if request.method == 'POST':
        timer_hour_aft = request.POST['daily_time_hour']
        timer_min_aft = request.POST['daily_time_min']
        daily_time_aft = timer_hour_aft + ":" + timer_min_aft
        daily_time_aft = pd.to_datetime(daily_time_aft, format="%H:%M", errors="coerce")
        if str(daily_time_aft) == "NaT":
            print(12)
            timer_hour_aft = "NaT"
            timer_min_aft = "输入错误"
            daily_time_aft = timer_hour_aft + ":" + timer_min_aft
            daily_time = daily_time_aft
        else:
            trig_time_aft = TrigTime(trig_time_hour=timer_hour_aft, trig_time_min=timer_min_aft)
            trig_time_aft.save()
            trig_time_aft = TrigTime.objects.last()
            daily_time = trig_time_aft.trig_time_hour + ":" + trig_time_aft.trig_time_min
    else:
        daily_time = daily_time_bef

    context = {
        'daily_time': daily_time,
    }
    return render(request, template_name='timer.html', context=context)


# bai_utl_str:百度地图天气API;per_utl_str:万年历天气API
def weather_data(request):
    # daily_time = "8:30"
    daily_time = the_daily_time
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
        'daily_time': daily_time,
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
