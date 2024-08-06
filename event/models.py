from django.db import models


# Create your models here.
class Event(models.Model):
    course = models.ForeignKey(
        "dashboard.Course", on_delete=models.CASCADE, related_name="c_events"
    )
    title = models.CharField(max_length=254)
    description = models.TextField()
    location = models.CharField(max_length=254)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    # TODO: Add frequency support for this event model
    # frequency = models
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
