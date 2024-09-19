from . import views
from django.urls import path

app_name = "inbox"

urlpatterns = [
    path("", views.InboxList.as_view(), name="inbox"),
    path("<int:inbox_id>/", views.InboxView.as_view(), name="inbox-view"),
    path("compose/", views.InboxCompose.as_view(), name="inbox-compose"),
]
