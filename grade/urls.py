from . import views
from django.urls import path

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

# professor url
urlpatterns += [
    path(
        "<int:course_id>/",
        views.GradeProfessorCourse.as_view(),
        name="grade-professor-course",
    ),
    path(
        "<int:course_id>/activity/<int:activity_id>/",
        views.GradeActivity.as_view(),
        name="grade-activity",
    ),
    path(
        "<int:course_id>/activity/<int:activity_id>/student/<int:student_id>/",
        views.GradeUpdateActivityScore.as_view(),
        name="grade-update-activity-score",
    ),
    path(
        "<int:course_id>/exam/<int:exam_id>/",
        views.GradeExam.as_view(),
        name="grade-exam",
    ),
    path(
        "<int:course_id>/exam/<int:exam_id>/student/<int:student_id>/",
        views.GradeUpdateExamScore.as_view(),
        name="grade-update-exam-score",
    ),
    path(
        "<int:course_id>/activity/add",
        views.GradeAddActivity.as_view(),
        name="grade-add-activity",
    ),
    path(
        "<int:course_id>/exam/add",
        views.GradeAddExam.as_view(),
        name="grade-add-exam",
    ),
]

# student url
urlpatterns += [
    path(
        "student/<int:course_id>/",
        views.GradeStudentCourse.as_view(),
        name="grade-student-course",
    ),
]
