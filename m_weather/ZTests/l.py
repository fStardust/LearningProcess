#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
from datetime import datetime, time

from debug_mail import mail


# 定义线程调用函数
class ThreadingTimer(threading.Thread):
    def run(self):
        while True:
            localtime = datetime.now()
            time_now = localtime.strftime("%S")  # 刷新
            if time_now == "20":
                print(localtime.strftime("%Y-%m-%d %H:%M:%S"))
                mail()
                time.sleep(2)

    # def run(self):
    #     while True:
    #         time_now = time.strftime("%H:%M", time.localtime())  # 刷新
    #         if time_now == "10:11":
    #             print("打开")
    #             print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    #             time.sleep(2)  # 因为以秒定时，所以暂停2秒，使之不会在1秒内执行多次
    #
    #         if user_choice == "C10A":  # 如果控制台输入C10A
    #             print("thread3 :线程退出")
    #             return


# 创建新线程
thread3 = ThreadingTimer()

thread3.start()
print("thread3 :线程打开")


# # ###################
# from datetime import datetime
#
# import pandas as pd
#
# localtime = datetime.now()
# time_now = localtime.strftime("%H:%M")
# daily_time = "12:00"
# try:
#     timeArray = datetime.strptime(daily_time, "%H:%M")
# except ValueError:
#     timeArray = pd.to_datetime(daily_time, format="%H:%M", errors="coerce")
#
# daily_time_hour = timeArray.hour
#
# print(daily_time_hour)

