import requests
from django.http import HttpResponse
from django.shortcuts import render
from .models import WeatherInfo
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect


from django.shortcuts import HttpResponse
from weather.myKey import KEY
import json


def index(request):
    def get(api_type):

        url_api_weather = 'https://devapi.qweather.com/v7/weather/'
        my_key = KEY
        city_id = '北京'
        middle = '&key='

        url = url_api_weather + api_type + '?location=' + city_id + middle + my_key
        # return requests.get(url).json()

    get_now = get('now')

    return HttpResponse(get_now)
