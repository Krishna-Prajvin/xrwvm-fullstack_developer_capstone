from django.contrib import admin
from .models import CarMake, CarModel

class CarMakeAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']

class CarModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'car_make', 'type', 'year', 'dealer_id']
    search_fields = ['name']

admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)
