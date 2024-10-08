from django.urls import path
from . import views

app_name = "announcement"

# URL PATTERN <int:announcement_id>
# Example: <int:announcement_id>/detail/ <int:announcement_id>/create/

# TODO: Add dynamic url after Samia Finish designing

urlpatterns = [
    path("", views.AnnouncementList.as_view(), name="announcement-list"),
    path(
        "<int:announcement_id>/",
        views.AnnouncementDetail.as_view(),
        name="announcement-detail",
    ),
    path("create/", views.AnnouncementCreate.as_view(), name="announcement-create"),
    path(
        "<int:announcement_id>/update/",
        views.AnnouncementUpdate.as_view(),
        name="announcement-update",
    ),
]
