from django.db import models


# Create your models here.
class Announcement(models.Model):
    course = models.ForeignKey(
        "dashboard.Course",
        on_delete=models.CASCADE,
        related_name="announcements",
    )
    title = models.CharField(max_length=254)
    content = models.TextField()
    posted_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
