from django.contrib import admin

from . import models


@admin.register(models.CitySearch)
class CitySearchAdmin(admin.ModelAdmin):
    list_display = (
        "city",
        "timestamp",
    )
