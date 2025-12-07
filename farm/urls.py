from rest_framework.routers import DefaultRouter
from django.urls import path, include
from farm import views

router = DefaultRouter() # CREATING A ROUTER INSTANCE
router.register(r'species', views.SpeciesViewSet) # REGISTERING SPECIES ENDPOINT
router.register(r'animals', views.AnimalViewSet) # REGISTERING ANIMALS ENDPOINT
router.register(r'foodstocks', views.FoodStockViewSet) # REGISTERING FOOD STOCK ENDPOINT
router.register(r'tasks', views.TasksViewSet) # REGISTERING TASKS ENDPOINT
router.register(r'healthlogs', views.HealthLogViewSet) # REGISTERING HEALTH LOGS ENDPOINT
router.register(r'productionlogs', views.ProductionLogViewSet) # REGISTERING PRODUCTION
router.register(r'weatherlogs', views.WeatherLogViewSet) # REGISTERING WEATHER LOGS ENDPOINT


urlpatterns = [
    path('', include(router.urls)), # INCLUDING ROUTER URLS
    path('api/animals/<int:animal_pk>/health/', views.HealthLogViewSet.as_view({'get':'list', 'post':'create'}), name='animal-health'), # NESTED ROUTE FOR ANIMAL HEALTH LOGS
]



