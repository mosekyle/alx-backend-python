from rest_framework import viewsets
from .models import User, Message, Conversation
from .serializers import UserSerializer, MessageSerializer, ConversationSerializer
from rest_framework import status
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    filterset_fields = ['participants']

    def create(self, request, *args, **kwargs):
        # Custom logic for creating a conversation can be added here
        return super().create(request, *args, **kwargs)

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    ordering_fields = '__all__'
    filterset_fields = ['conversation']

    def create(self, request, *args, **kwargs):
        # Custom logic for sending a message can be added here
        return super().create(request, *args, **kwargs)

