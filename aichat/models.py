from django.db import models

# Create your models here.
class ChatHistory(models.Model):
    user_message = models.TextField()
    ai_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Chat at {self.timestamp}"