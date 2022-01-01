from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('qWeather/', include('qWeather.urls')),
    path('nWeather/', include('nWeather.urls')),
    path('admin/', admin.site.urls),
]