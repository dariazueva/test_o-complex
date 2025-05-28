from django.test import Client, TestCase
from django.urls import reverse

from .models import CitySearch


class WeatherViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_view_get(self):
        response = self.client.get(reverse("index"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "weather/index.html")

    def test_weather_view_valid_city(self):
        response = self.client.post(reverse("weather"), data={"city": "Москва"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("Погода в", response.content.decode())

    def test_weather_view_invalid_city(self):
        response = self.client.post(reverse("weather"), data={"city": "НеверныйГород"})
        self.assertEqual(response.status_code, 200)
        self.assertIn("не удалось найти город", response.content.decode().lower())

    def test_city_search_model(self):
        CitySearch.objects.create(city="Тестгород")
        self.assertEqual(CitySearch.objects.count(), 1)
        self.assertEqual(CitySearch.objects.first().city, "Тестгород")

    def test_city_stats_api_view(self):
        CitySearch.objects.create(city="Москва")
        CitySearch.objects.create(city="Москва")
        CitySearch.objects.create(city="Питер")
        response = self.client.get(reverse("city_stats"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("Москва", response.content.decode())
