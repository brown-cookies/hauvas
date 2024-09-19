from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.TodoList.as_view(), name="todo"),
    path("create/", views.TodoCreate.as_view(), name="todo-create"),
    path("<int:todo_id>/", views.TodoDetail.as_view(), name="todo-detail"),
    path("<int:todo_id>/update/", views.TodoUpdate.as_view(), name="todo-update"),
]
