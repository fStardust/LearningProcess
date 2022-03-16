#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

from communication import com_weather

localtime = time.localtime(time.time())  # 创建时间对象

daily_time = "20"


# 定义线程调用函数
class ThreadingTimer(threading.Thread):
    def run(self):
        while True:
            time_now = time.strftime("%S", time.localtime())  # 刷新
            if time_now == daily_time:
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
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
day_timer = ThreadingTimer()

day_timer.start()
print("day_timer :线程打开")  # --
