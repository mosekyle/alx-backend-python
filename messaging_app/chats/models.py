from django.db import models
import uuid
from django.contrib.auth.models import AbstractUser

# User Model
class User(AbstractUser):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    role_choices = [
        ('guest', 'Guest'),
        ('host', 'Host'),
        ('admin', 'Admin')
    ]
    role = models.CharField(max_length=5, choices=role_choices, default='guest')
    
    # Optionally, add additional fields
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Conversation Model
class Conversation(models.Model):
    conversation_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    participants = models.ManyToManyField(User)  # Many-to-many relationship with User
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Conversation {self.conversation_id}"

# Message Model
class Message(models.Model):
    message_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    sender = models.ForeignKey(User, related_name='sent_messages', on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    message_body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} in conversation {self.conversation_id}"

