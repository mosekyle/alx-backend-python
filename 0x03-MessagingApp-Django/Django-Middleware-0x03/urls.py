from django.contrib import admin
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from django.urls import path, include

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/', include('chats.urls')),  # Include chats app URLs
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),  # Add the API auth routes

]

