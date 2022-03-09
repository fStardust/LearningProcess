#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

# 全国天气预报_获取城市
if __name__ == '__main__':
    url = 'http://m.weather.com.cn/data/'

    headers = {

        'Content-Type': 'application/json:charset=UTF-8',
        'X-Bce-Signature': ''
    }
    r = requests.request("GET", url)
    print(r.content)
