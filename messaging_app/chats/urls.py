from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConversationViewSet, MessageViewSet

# Instantiate the DefaultRouter
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Define the urlpatterns
urlpatterns = [
    path('', include(router.urls)),  # Include the router's URLs
]

