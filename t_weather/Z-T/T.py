#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:XXX

Tdict = {'code': '200', 'updateTime': '2022-03-09T21:22+08:00', 'fxLink': 'http://hfx.link/2ax1', 'now': {'obsTime': '2022-03-09T21:12+08:00', 'temp': '12', 'feelsLike': '11', 'icon': '502', 'text': '霾', 'wind360': '90', 'windDir': '东风', 'windScale': '1', 'windSpeed': '4', 'humidity': '56', 'precip': '0.0', 'pressure': '1011', 'vis': '3', 'cloud': '100', 'dew': '2'}, 'refer': {'sources': ['QWeather', 'NMC', 'ECMWF'], 'license': ['no commercial use']}}
print(Tdict['code'])
Tnow = Tdict.get('now')
print(Tnow.get('temp'))