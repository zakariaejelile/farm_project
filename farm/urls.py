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
    #dashboard and CRUD
    path('dashboard/', views.dashboard, name='dashboard'),

    path('animals/', views.animal_list, name='animal_list'),
    path('animals/new/', views.animal_create, name='animal_create'),
    path("animals/<int:pk>/", views.animal_detail, name="animal_detail"),
    path("animals/<int:pk>/edit/", views.animal_update, name="animal_update"),
    path("animals/<int:pk>/delete/", views.animal_delete, name="animal_delete"),

    path('food/', views.food_stock, name='food_stock'),
    path('food/new/', views.food_stock_create, name='food_stock_create'),
    path('food/<int:pk>/', views.food_stock_detail, name='food_stock_detail'),
    path('food/<int:pk>/edit/', views.food_stock_update, name='food_stock_update'),
    path('food/<int:pk>/delete/', views.food_stock_delete, name='food_stock_delete'),

    path('tasks/', views.task_list, name='task_list'),
    path("tasks/new/", views.task_create, name="task_create"),  
    path('tasks/<int:pk>/', views.task_detail, name='task_detail'),
    path('tasks/<int:pk>/delete/', views.task_delete, name='task_delete'),
    path('tasks/<int:pk>/edit/', views.task_update, name='task_update'),

    path('production/', views.production_list, name='production_list'),
    path('production/new/', views.production_create, name='production_create'),
    path('production/<int:pk>/', views.production_detail, name='production_detail'),
    path('production/<int:pk>/edit/', views.production_update, name='production_update'),
    path('production/<int:pk>/delete/', views.production_delete, name='production_delete'),

    path('healthlogs/', views.health_log_list, name='health_log_list'),
    path('healthlogs/new/', views.health_log_create, name='health_log_create'),
    path('healthlogs/<int:pk>/', views.health_log_detail, name='health_log_detail'),
    path('healthlogs/<int:pk>/edit/', views.health_log_update, name='health_log_update'),
    path('healthlogs/<int:pk>/delete/', views.health_log_delete, name='health_log_delete'),

    path('weather/', views.weather_data, name='weather_data'),

    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    #API 
    path('api/', include(router.urls)),

    #NESTED API
    path(
        'api/animals/<int:animal_pk>/health/',
        views.HealthLogViewSet.as_view({'get': 'list', 'post': 'create'}), name='animal-health'),
]


