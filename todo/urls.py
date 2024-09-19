from django.urls import path
from . import views

app_name = "todo"

urlpatterns = [
    path("", views.TodoList.as_view(), name="todo"),
    path(
        "<int:todo_id>/toggle/", views.TodoToggleCheckbox.as_view(), name="todo-toggle"
    ),
    path("<int:todo_id>/delete/", views.TodoTrash.as_view(), name="todo-delete"),
]
