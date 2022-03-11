import numpy as np

import pandas as pd

# 读取cvs文件
city_file = "./static/weather_district_id.csv"
city_csv = pd.read_csv(city_file)


city = "北京"
for i in range(len(city_csv)):
    if city_csv['district'][i] == city:
        print(city_csv['district_geocode'][i])
