def com_weather():
    global my_sender, my_pass, my_user
    import json
    import smtplib
    from email.mime.text import MIMEText
    from email.utils import formataddr
    import pandas as pd
    import requests
    import xmltodict
    my_sender = '2111732367@qq.com'  # 填写发信人的邮箱账号
    my_pass = 'tcfajvsggnwodehi'  # 发件人邮箱授权码
    my_user = 'xingichen@126.com'  # 收件人邮箱账号

    def the_mail_data():
        global per_detail
        city_file = "../information/weather_district_id.csv"
        city_csv = pd.read_csv(city_file)
        ip_api = 'https://api.map.baidu.com/location/ip?ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
        bai_response = requests.get(ip_api)
        city_dict = json.loads(bai_response.text)
        current_location = city_dict['content']['address_detail']['city']
        for i in range(len(city_csv)):
            if current_location == str(city_csv['city'][i]):
                districtcode = str(city_csv['districtcode'][i])
                citycode = str(city_csv['areacode'][i])
                break
        bai_utl_str = 'https://api.map.baidu.com/weather/v1/?district_id=' + districtcode + '&data_type=all&ak=b78I1MmxAMts1dkuBrwhyahPE6V6y5I7'
        per_utl_str = 'http://wthrcdn.etouch.cn/WeatherApi?citykey=' + citycode
        bai_response = requests.get(bai_utl_str).text
        per_response = requests.get(per_utl_str, verify=False).text
        bai_weather_dict = json.loads(bai_response)
        per_weather_dict = json.loads(json.dumps(xmltodict.parse(per_response)))
        data_dict = bai_weather_dict['result']
        w_date = data_dict['forecasts'][0]
        n_date = data_dict['now']
        province = data_dict['location']['province']
        city = data_dict['location']['city']
        current_location = "您目前所在位置为:" + current_location + province + city
        now_text = "当前天气状况：" + n_date["text"]
        now_temp = "当前气温：" + str(n_date["temp"]) + "℃"
        now_sensible_temp = "当前体感温度：" + str(n_date["feels_like"]) + "℃"
        now_rh = "当前环境相对湿度：" + str(n_date["rh"]) + "%"
        now_wind_dir = "当前风向：" + n_date["wind_dir"]
        now_wind_class = "当前风速" + n_date["wind_class"]
        per_recommend = "推荐外出穿着——" + per_weather_dict["resp"]["zhishus"]["zhishu"][0]["detail"]
        today_text = "**********今日天气状况**********"
        today_date = "--" + w_date['text_day'] + "----" + w_date['week'] + "--"
        today_text_day = "今日白天天气状况：" + w_date['text_day']
        today_text_night = "今日晚间天气状况：" + w_date['text_night']
        today_high = "今日最高温度：" + str(w_date['high']) + "℃"
        today_low = "今日最低温度：" + str(w_date['low']) + "℃"
        today_wd_day = "今日白天风向：" + w_date['wd_day']
        today_wc_day = "今日白天风速：" + str(w_date['wc_day'])
        today_wd_night = "今日晚间风向：" + w_date['wd_night']
        today_wc_night = "今日晚间风速：" + str(w_date['wc_night'])
        mail_weather_data = []
        for i in current_location, now_text, now_temp, now_sensible_temp, now_rh, now_wind_dir, now_wind_class, per_recommend, today_text, today_date, today_text_day, today_text_night, today_high, today_low, today_wd_day, today_wc_day, today_wd_night, today_wc_night:
            mail_weather_data.append(i)
        per_detail = ""
        for n in mail_weather_data:
            per_detail += n  # 取出API建议字典各模块中detail内容
            per_detail += "\n"
        return per_detail

    def mail(data):
        ret = True
        try:
            msg = MIMEText(data, 'plain', 'utf-8')  # 邮件内容
            msg['From'] = formataddr(["个性化天气预报系统", my_sender])  # 发件人邮箱昵称、发件人邮箱账号
            msg['To'] = formataddr(["用户您好", my_user])  # 收件人邮箱昵称、收件人邮箱账号
            msg['Subject'] = "今日气温与外出着装建议"  # 邮件主题

            server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # SMTP服务器
            server.login(my_sender, my_pass)
            server.sendmail(my_sender, [my_user, ], msg.as_string())
            server.quit()  # 关闭连接
        except Exception:
            ret = False
        if ret:
            print("邮件发送成功")
        else:
            print("邮件发送失败")
        return ret

    the_mail_data()
    mail(per_detail)


# com_weather()
