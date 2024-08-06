from django.db import models
from django.conf import settings


# Create your models here.
class Todo(models.Model):
    course = models.ForeignKey(
        "dashboard.Course", on_delete=models.CASCADE, related_name="c_todos"
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="todos"
    )
    title = models.CharField(max_length=254)
    description = models.TextField()
    due_date = models.DateTimeField()
    is_complete = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
