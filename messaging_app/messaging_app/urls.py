from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('chats.urls')),  # Include the API routes
    path('api-auth/', include('rest_framework.urls')),  # Add the API auth routes
]

