# CHECKING IF THE DATABASE IS WORKING PROPELY
from django.contrib import admin
from .models import Animal, HealthLog, WeatherLog, ProductionLog, Tasks, FoodStock, Species

admin.site.register(Animal)
admin.site.register(WeatherLog)
admin.site.register(HealthLog)
admin.site.register(ProductionLog)
admin.site.register(Tasks)
admin.site.register(FoodStock)
admin.site.register(Species)


