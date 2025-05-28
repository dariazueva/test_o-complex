from http import HTTPStatus

import requests
from django.conf import settings
from django.db.models import Count
from django.shortcuts import redirect, render

from .forms import CityForm
from .models import CitySearch

WEATHER_API_KEY = settings.WEATHER_API_KEY


def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric&lang=ru"
    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code != HTTPStatus.OK:
            return {"error": "Не удалось найти город."}
        return {
            "temperature": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"],
        }
    except Exception:
        return {"error": "Произошла ошибка при получении данных о погоде."}


def index(request):
    form = CityForm()
    return render(request, "weather/index.html", {"form": form})


def weather_view(request):
    if request.method == "POST":
        form = CityForm(request.POST)
        if form.is_valid():
            city = form.cleaned_data["city"]
            weather = get_weather(city)
            if "error" not in weather:
                CitySearch.objects.create(city=city)
                return render(
                    request, "weather/result.html", {"city": city, "weather": weather}
                )
            return render(
                request, "weather/index.html", {"form": form, "error": weather["error"]}
            )
    return redirect("index")


def city_stats_api(request):
    stats = (
        CitySearch.objects.values("city")
        .annotate(count=Count("city"))
        .order_by("-count")
    )
    return render(request, "weather/stats.html", {"stats": stats})
