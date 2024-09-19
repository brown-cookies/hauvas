from . import views
from django.urls import path

app_name = "inbox"

urlpatterns = [
    path("", views.InboxList.as_view(), name="inbox"),
    path("compose/", views.InboxCompose.as_view(), name="inbox-compose"),
    path("<int:inbox_id>/", views.InboxView.as_view(), name="inbox-view"),
    path(
        "<int:inbox_id>/starred/",
        views.InboxMarkAsStarred.as_view(),
        name="inbox-toggle-starred",
    ),
    path(
        "<int:inbox_id>/archived/",
        views.InboxMarkAsArchived.as_view(),
        name="inbox-toggle-archived",
    ),
    path("<int:inbox_id>/trashed/", views.InboxTrashed.as_view(), name="inbox-trashed"),
]
