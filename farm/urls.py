from django.urls import path, include
from rest_framework.routers import DefaultRouter
from farm import views
from django.contrib.auth.views import LogoutView



# API ROUTER
router = DefaultRouter()
router.register(r'species', views.SpeciesViewSet)
router.register(r'animals', views.AnimalViewSet)
router.register(r'foodstocks', views.FoodStockViewSet)
router.register(r'tasks', views.TasksViewSet)
router.register(r'healthlogs', views.HealthLogViewSet)
router.register(r'productionlogs', views.ProductionLogViewSet)
router.register(r'weatherlogs', views.WeatherLogViewSet)


# URL PATTERNS
urlpatterns = [
    #(HTML)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('animals/', views.animal_list, name='animal_list'),
    path('animals/new/', views.animal_create, name='animal_create'),
    path('food/', views.food_stock, name='food_stock'),
    path('tasks/', views.task_list, name='task_list'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #API 
    path('api/', include(router.urls)),

    #NESTED API
    path(
        'api/animals/<int:animal_pk>/health/',
        views.HealthLogViewSet.as_view({'get': 'list', 'post': 'create'}), name='animal-health'),
]


