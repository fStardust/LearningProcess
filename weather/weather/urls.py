from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('qWeather/', include('qWeather.urls')),
    path('nWeather/', include('nWeather.urls')),
]
