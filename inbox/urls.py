from django.urls import path
from . import views

app_name = "inbox"

urlpatterns = [
    path("", views.InboxList.as_view(), name="inbox"),
    path("<int:inbox_id>/", views.InboxView.as_view(), name="inbox-view"),
    path("compose/", views.InboxCompose.as_view(), name="inbox-compose"),
]
