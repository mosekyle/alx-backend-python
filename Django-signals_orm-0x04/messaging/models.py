from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    edited = models.BooleanField(default=False)
    edited_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='edited_messages')  # Tracks who edited the messagefrom django.db import models
    read = models.BooleanField(default=False)  # Field to indicate if the message has been read
    objects = models.Manager()  # Default manager
    unread = UnreadMessagesManager()  # Custom manager for unread messages
    parent_message = models.ForeignKey(
        'self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE
    )

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

    def get_thread(self):
        """
        Recursively fetch all replies to this message in a threaded format.
        """
        thread = [self]
        for reply in self.replies.all():
            thread.extend(reply.get_thread())
        return thread

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"`
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"Notification for {self.user} - Message from {self.message.sender}"
class MessageHistory(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='history')
    old_content = models.TextField()
    edited_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"History for Message ID {self.message.id}"
class UnreadMessagesManager(models.Manager):
    def for_user(self, user):
        return self.filter(receiver=user, read=False).only('id', 'sender', 'content', 'timestamp')

