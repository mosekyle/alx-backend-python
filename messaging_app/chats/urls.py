from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ConversationViewSet, MessageViewSet

# Instantiate the DefaultRouter
router = DefaultRouter()

# Register your viewsets with the router
router.register(r'conversations', ConversationViewSet, basename='conversation')
router.register(r'messages', MessageViewSet, basename='message')

# Include the router's URLs in urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]

