#!/usr/bin/python
# -*- coding: UTF-8 -*-
import threading
import time
from datetime import datetime

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


# 创建新线程
thread3 = ThreadingTimer()

thread3.start()
print("thread3 :线程打开")
