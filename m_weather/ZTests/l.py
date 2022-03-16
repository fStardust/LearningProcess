from datetime import datetime
import time

'''
每个 10 秒打印当前时间。
'''
now_time = datetime.now()
aim_time = "9:00"

def timedTask():
    while True:


        print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        time.sleep(10)


if __name__ == '__main__':
    timedTask()