from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import User, Conversation, Message
from .serializers import UserSerializer, ConversationSerializer, MessageSerializer

# Conversation ViewSet
class ConversationViewSet(viewsets.ModelViewSet):
    queryset = Conversation.objects.all()
    serializer_class = ConversationSerializer

    def create(self, request, *args, **kwargs):
        participants = request.data.get('participants')
        if not participants:
            return Response({'error': 'Participants are required'}, status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.create()
        for user_id in participants:
            user = User.objects.get(user_id=user_id)
            conversation.participants.add(user)
        conversation.save()

        return Response(ConversationSerializer(conversation).data, status=status.HTTP_201_CREATED)

# Message ViewSet
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def create(self, request, *args, **kwargs):
        conversation_id = request.data.get('conversation_id')
        sender_id = request.data.get('sender_id')
        message_body = request.data.get('message_body')

        if not conversation_id or not sender_id or not message_body:
            return Response({'error': 'All fields are required'}, status=status.HTTP_400_BAD_REQUEST)

        conversation = Conversation.objects.get(conversation_id=conversation_id)
        sender = User.objects.get(user_id=sender_id)
        message = Message.objects.create(conversation=conversation, sender=sender, message_body=message_body)

        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

