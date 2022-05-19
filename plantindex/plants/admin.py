from django.contrib import admin

from .models import Plant

@admin.register(Plant)

class PlantAdmin(admin.ModelAdmin):
    list_display = ['name', 'genus', 'plant_img', 'description', 'category']

