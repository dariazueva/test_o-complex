from django.db import models


class CitySearch(models.Model):
    city = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Поиск города"
        verbose_name_plural = "Поиск городов"

    def __str__(self):
        return f"{self.city} @ {self.timestamp}"
