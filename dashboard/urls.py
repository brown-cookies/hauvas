from django.urls import path
from .views.announcement import Announcement
from .views.assignment import Assignment
from .views.views import Dashboard
from .views.home import Home
from .views.module import Module, ModuleDetail
from .views.syllabus import Syllabus


app_name = "dashboard"

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
    path("course/<int:course_id>/home/", Home.as_view(), name="course-home"),
    path(
        "course/<int:course_id>/syllabus/", Syllabus.as_view(), name="course-syllabus"
    ),
    path(
        "course/<int:course_id>/announcements/",
        Announcement.as_view(),
        name="course-announcement",
    ),
    path("course/<int:course_id>/modules/", Module.as_view(), name="course-module"),
    path(
        "course/<int:course_id>/modules/<int:module_id>/",
        ModuleDetail.as_view(),
        name="course-module-detail",
    ),
    path(
        "course/<int:course_id>/assignments/",
        Assignment.as_view(),
        name="course-assignment",
    ),
]
