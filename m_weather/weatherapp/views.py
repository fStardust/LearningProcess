import json
import os
import random
from datetime import datetime

import pandas as pd
import requests
import xmltodict
from apscheduler.schedulers.background import BackgroundScheduler
from django.shortcuts import render
from django_apscheduler.jobstores import DjangoJobStore, register_job

from weatherMail.communication import com_weather
from weatherapp.method import get_rick_area
from weatherapp.models import TrigTime, LogSheet, Recommend, Condition

city_file = os.path.abspath('.\information\weather_district_id.csv')
city_csv = pd.read_csv(city_file)

trig_time = TrigTime.objects.last()
test_id = "timer" + str(trig_time.id) + chr((trig_time.id % 26) + 65) + chr(random.randint(65, 90))
timer_hour = trig_time.trig_time_hour
timer_min = trig_time.trig_time_min
the_daily_time = timer_hour + ":" + timer_min

# 定时触发
scheduler = BackgroundScheduler()
scheduler.add_jobstore(DjangoJobStore(), "default")


@register_job(scheduler, 'cron', day_of_week='*', hour=timer_hour, minute=timer_min, id=test_id)
def com_timer():
    localtime = datetime.now()
    log_sheet = LogSheet(run_time=localtime, choice_text="text")
    log_sheet.save()
    com_weather()


scheduler.start()  # 开始执行调度器

get_rick_area()  # 获取国内中高风险地区 并保存在 全国最先风险等级区域.csv


# 修改定时提醒时间
def change_time(request):
    trig_time_now = TrigTime.objects.last()
    timer_hour_now = trig_time_now.trig_time_hour
    timer_min_now = trig_time_now.trig_time_min
    the_daily_time_now = timer_hour_now + ":" + timer_min_now
    daily_time_bef = the_daily_time_now
    if request.method == 'POST':
        timer_hour_aft = request.POST['daily_time_hour']
        timer_min_aft = request.POST['daily_time_min']
        daily_time_aft = timer_hour_aft + ":" + timer_min_aft
        daily_time_aft = pd.to_datetime(daily_time_aft, format="%H:%M", errors="coerce")
        if str(daily_time_aft) == "NaT":
            timer_hour_aft = "NaT"
            timer_min_aft = "输入错误"
            daily_time_aft = timer_hour_aft + ":" + timer_min_aft
            daily_time = daily_time_aft
        else:
            # trig_time_aft = TrigTime.objects.last()
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
    trig_time_now = TrigTime.objects.last()
    # test_id = "timer" + str(trig_time.id) + chr((trig_time.id % 26) + 65) + chr(random.randint(65, 90))
    timer_hour_now = trig_time_now.trig_time_hour
    timer_min_now = trig_time_now.trig_time_min
    the_daily_time_now = timer_hour_now + ":" + timer_min_now
    daily_time = the_daily_time_now
    print(daily_time)
    ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
    bai_response = requests.get(ip_api, verify=False).text
    city_dict = json.loads(bai_response)
    print(city_dict)
    current_location = city_dict['content']['address_detail']['city']
    district_l = str(city_dict['content']['address_detail']['city_code'])
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
    data_dict = bai_weather_dict["result"]
    w_date = data_dict['forecasts']

    bai_weather_json = json.dumps(bai_weather_dict, ensure_ascii=False)
    per_weather_json = json.dumps(per_weather_dict, ensure_ascii=False)

    p_city = data_dict['location']['province']
    b_city = data_dict['location']['city']
    m_city = data_dict['location']['name']
    city = "省级:" + p_city + ",市级：" + b_city + ",县市级：" + m_city
    print('城市：{}'.format(city))

    per_rec = per_weather_dict["resp"]["zhishus"]["zhishu"]

    per_utl_str_location = 'http://wthrcdn.etouch.cn/WeatherApi?city=' + current_location
    per_response_location = requests.get(per_utl_str_location, verify=False).text
    per_weather_dict_location = json.loads(json.dumps(xmltodict.parse(per_response_location)))
    per_rec_loc = per_weather_dict_location["resp"]["zhishus"]["zhishu"]

    # per_recommend_aft = ""
    # for i in per_rec:
    #     m = i['name'] + ':' + "|—————" + i['detail'] + '|____________|'
    #     per_recommend_aft = per_recommend_aft + m
    per_recommend_aft = per_rec[0]['name'] + ":" + per_rec[0]['detail']

    # recommend_loc = ""
    # for i in per_rec_loc:
    #     m = i['name'] + ':' + "|—————" + i['detail'] + '|____________|'
    #     recommend_loc = recommend_loc + m
    # recommend = recommend_loc
    recommend = per_rec_loc[0]['name'] + ":" + per_rec_loc[0]['detail']

    # 体感温度
    feels_like = str(data_dict['now']['feels_like']) + "℃"

    # 个人推荐值
    self_ind_l = Condition.objects.last()
    self_ind = self_ind_l.self_index
    all_ind = Recommend.objects.all()
    print(self_ind)
    if -10 < self_ind < 10:
        self_recommend = all_ind.all()[0].rec_data
    elif 10 <= self_ind < 20:
        self_recommend = all_ind.all()[1].rec_data
    elif 20 <= self_ind < 30:
        self_recommend = all_ind.all()[2].rec_data
    elif 30 <= self_ind < 40:
        self_recommend = all_ind.all()[3].rec_data
    elif 40 <= self_ind < 50:
        self_recommend = all_ind.all()[4].rec_data
    elif self_ind >= 50:
        self_recommend = all_ind.all()[5].rec_data
    elif -20 < self_ind <= -10:
        self_recommend = all_ind.all()[6].rec_data
    elif -30 < self_ind <= -20:
        self_recommend = all_ind.all()[7].rec_data
    elif -40 < self_ind <= -30:
        self_recommend = all_ind.all()[8].rec_data
    elif -50 < self_ind <= -40:
        self_recommend = all_ind.all()[9].rec_data
    else:
        self_recommend = all_ind.all()[10].rec_data

    travel_recommend = per_recommend_aft  # 旅游推荐

    nowtq = w_date[0]  # 改为 ***_weather
    onetq = w_date[1]
    twotq = w_date[2]
    threetq = w_date[3]
    fourtq = w_date[4]
    for item_dict1 in w_date:
        date = item_dict1['date']
        high = str(item_dict1['high']) + "℃"
        low = str(item_dict1['low']) + "℃"
        text_day = item_dict1['text_day']
        wd_day = item_dict1['wd_day']
        wc_day = item_dict1['wc_day']
        text_night = item_dict1['text_night']
        print(
            '时间：{}; 最高温度：{};最低温度：{}; 白天天气：{}; 白天风向：{};白天风速：{}; 晚间天气：{}'.format(
                date, high, low, text_day, wd_day, wc_day, text_night
            )
        )

    context = {
        'city': city,
        'weather_list': w_date,
        'daily_time': daily_time,
        'feels_like': feels_like,
        'nowtq': nowtq,
        'onetq': onetq,
        'twotq': twotq,
        'threetq': threetq,
        'fourtq': fourtq,
        'current_location': current_location,
        'recommend': recommend,
        'self_recommend': self_recommend,
        'travel_recommend': travel_recommend,
    }

    return render(request, template_name='weather.html', context=context)


# 个人感受反馈
def feedblack(request):
    self_ind = Condition.objects.last()
    self_index_bef = self_ind.self_index
    if request.method == 'POST':
        self_index_aft = self_index_bef + int(request.POST['self_index_change'])
        self_ind.self_index = self_index_aft
        self_ind.save()
        self_ind = Condition.objects.last()
        self_index_d = self_ind.self_index
    else:
        self_index_d = self_index_bef

    context = {
        "self_index_d": self_index_d
    }
    return render(request, template_name='feedblack.html', context=context)
