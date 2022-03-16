import time
localtime = time.localtime(time.time())
time_now = time.strftime("%H:%M", time.localtime())
daily_time = "12:00"
try:
    timeArray = time.strptime(daily_time, "%H:%M")
except:
    timeArray = time.strptime("00:00", "%H:%M")

daily_time_hour = timeArray.tm_hour

print(daily_time_hour)
