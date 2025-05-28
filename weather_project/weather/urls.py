from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("weather/", views.weather_view, name="weather"),
    path("stats/", views.city_stats_api, name="city_stats"),
]
