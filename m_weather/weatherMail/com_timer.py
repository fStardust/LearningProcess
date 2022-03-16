#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
from datetime import datetime

from communication import com_weather
from weatherapp.views import daily_timer


# 定义线程调用函数
class ThreadingTimer(threading.Thread):
    def run(self):
        while True:
            localtime = datetime.now()
            time_now = localtime.strftime("%S")  # 刷新
            if time_now == daily_timer:
                print(localtime.strftime("%Y-%m-%d %H:%M:%S"))
                com_weather()
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
ThreadingTimer().start()

print("day_timer :线程打开")  # --
