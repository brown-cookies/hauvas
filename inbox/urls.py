from django.urls import path
from . import views

app_name = "inbox"

urlpatterns = [path("", views.InboxList.as_view(), name="inbox")]
