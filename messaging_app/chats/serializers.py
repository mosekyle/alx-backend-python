from rest_framework import serializers
from .models import User, Conversation, Message
from django.contrib.auth.models import User as DjangoUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = DjangoUser  # Using the built-in User model for authentication
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'role']

class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)  # Nesting UserSerializer to display sender info
    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at', 'conversation']

class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True, read_only=True)  # Display participants in the conversation
    messages = MessageSerializer(many=True, read_only=True)  # Nested messages in the conversation
    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'messages', 'created_at']
