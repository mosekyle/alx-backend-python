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

