from django.urls import path
from . import views

urlpatterns = [
    path('weather/', views.get_weather, name='get_weather'),
]
# Django settings for weather_project project.