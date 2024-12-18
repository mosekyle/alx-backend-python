from rest_framework import serializers
from .models import User, Conversation, Message

# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_id', 'first_name', 'last_name', 'email', 'phone_number', 'role']

# Message Serializer
class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.CharField(source='sender.email')  # Display sender's email

    class Meta:
        model = Message
        fields = ['message_id', 'sender', 'message_body', 'sent_at']

# Conversation Serializer
class ConversationSerializer(serializers.ModelSerializer):
    participants = UserSerializer(many=True)  # Include user details for participants
    messages = MessageSerializer(many=True, read_only=True)  # Include messages in the conversation

    class Meta:
        model = Conversation
        fields = ['conversation_id', 'participants', 'created_at', 'messages']

