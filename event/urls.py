from django.urls import path
from . import views

app_name = "event"

# URL PATTERN <int:event_id>
# Example: <int:event_id>/detail/ <int:event_id>/create/

# TODO: Add dynamic url after Sicat Finish designing

urlpatterns = [
    path("", views.EventList.as_view(), name="event-list"),
    path("detail/", views.EventDetail.as_view(), name="event-detail"),
    path("create/", views.EventCreate.as_view(), name="event-create"),
    path("update/", views.EventUpdate.as_view(), name="event-update"),
]
