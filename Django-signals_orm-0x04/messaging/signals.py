from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Message, MessageHistory

@receiver(pre_save, sender=Message)
def log_message_edit(sender, instance, **kwargs):
    if instance.pk:  # Ensure this is an update, not a new instance
        original_message = Message.objects.get(pk=instance.pk)
        if original_message.content != instance.content:  # Check if content is changed
            MessageHistory.objects.create(
                message=original_message,
                old_content=original_message.content
            )
            instance.edited = True  # Mark the message as edited
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from messaging.models import Message, Notification, MessageHistory

@receiver(post_delete, sender=User)
def delete_user_related_data(sender, instance, **kwargs):
    # Delete messages where the user is the sender or receiver
    Message.objects.filter(sender=instance).delete()
    Message.objects.filter(receiver=instance).delete()
    
    # Delete notifications related to the user
    Notification.objects.filter(user=instance).delete()
    
    # Delete message history related to the user
    MessageHistory.objects.filter(message__sender=instance).delete()
    MessageHistory.objects.filter(message__receiver=instance).delete()

