from django.contrib import admin
from api.models import Bike
# Register your models here.
@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ['id','bike_name','bike_model','bike_cc','bike_average']