from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),         # homepage
    path('api/', views.get_weather, name='api'), # api endpoint
]
