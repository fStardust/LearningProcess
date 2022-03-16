#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time

from debug_mail import mail

localtime = time.localtime(time.time())  # 创建时间对象


# 定义线程调用函数
class ThreadingTimer(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        while True:
            time_now = time.strftime("%S", time.localtime())  # 刷新
            if time_now == "30":
                print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
                mail()
                time.sleep(2)


# 创建新线程
thread3 = threading_timer(3, "heWaterHeaterAuto", 3)

while True:
    user_choice = input()
    if user_choice == "C11A":  # 如果控制台输入C11A
        thread3.start()
        print("thread3 :线程打开")
