from django.urls import path
from . import views

app_name = "grade"

# URL PATTERN <int:grade_id>
# Example: <int:grade_id>/detail/ <int:grade_id>/create/

# TODO: Add dynamic url after Chin Finish designing

urlpatterns = [
    path("", views.GradeList.as_view(), name="grade-list"),
    path("detail/", views.GradeDetail.as_view(), name="grade-detail"),
    path("create/", views.GradeCreate.as_view(), name="grade-create"),
    path("update/", views.GradeUpdate.as_view(), name="grade-update"),
]
