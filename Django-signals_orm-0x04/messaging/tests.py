from django.test import TestCase
from django.contrib.auth.models import User
from .models import Message, Notification

class MessagingTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')

    def test_notification_creation(self):
        message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello!")
        notification = Notification.objects.get(user=self.user2)
        self.assertEqual(notification.message, message)
        self.assertFalse(notification.is_read)
class MessageEditTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        self.message = Message.objects.create(sender=self.user1, receiver=self.user2, content="Initial content")

    def test_message_edit_logs_history(self):
        self.message.content = "Updated content"
        self.message.save()
        history = MessageHistory.objects.filter(message=self.message)
        self.assertEqual(history.count(), 1)
        self.assertEqual(history.first().old_content, "Initial content")
        self.assertTrue(self.message.edited)

class UnreadMessagesManagerTests(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(username='user1', password='password')
        self.user2 = User.objects.create_user(username='user2', password='password')
        Message.objects.create(sender=self.user1, receiver=self.user2, content="Hello!", read=False)
        Message.objects.create(sender=self.user1, receiver=self.user2, content="Hi again!", read=True)

    def test_unread_messages_for_user(self):
        unread_messages = Message.unread.for_user(self.user2)
        self.assertEqual(unread_messages.count(), 1)
        self.assertEqual(unread_messages.first().content, "Hello!")
