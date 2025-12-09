from django.contrib import admin
from django.urls import path ,include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),

    # Including farm app URLs
    path('', include('farm.urls')),

    # Authentication URLs
    path('accounts/', include('django.contrib.auth.urls')),  #  LOGIN / LOGOUT,
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]

