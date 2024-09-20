from django.conf import settings
from django.db import models


# Create your models here.
class Inbox(models.Model):
    sender = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="sender"
    )
    receiver = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="receiver"
    )
    is_starred = models.BooleanField(default=False)
    is_trashed = models.BooleanField(default=False)
    subject = models.CharField(max_length=254)
    content = models.TextField()
    is_archived = models.BooleanField(default=False)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"from {self.sender} to {self.receiver} - {self.subject}"
