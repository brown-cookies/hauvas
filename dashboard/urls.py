from django.urls import path
from .views.announcement import Announcement
from .views.assignment import Assignment
from .views.views import Dashboard
from .views.home import Home, HomeUpdate
from .views.syllabus import Syllabus
from .views.people import PeopleList
from .views.module import Module, ModuleDetail


app_name = "dashboard"

homeurls = [
    path("course/<int:course_id>/home/", Home.as_view(), name="course-home"),
    path(
        "course/<int:course_id>/home/update/",
        HomeUpdate.as_view(),
        name="course-home-update",
    ),
]

syllabusurls = [
    path(
        "course/<int:course_id>/syllabus/", Syllabus.as_view(), name="course-syllabus"
    ),
]

peopleurls = [
    path("course/<int:course_id>/people/", PeopleList.as_view(), name="course-people")
]

announcementurls = [
    path(
        "course/<int:course_id>/announcements/",
        Announcement.as_view(),
        name="course-announcement",
    ),
]

moduleurls = [
    path("course/<int:course_id>/modules/", Module.as_view(), name="course-module"),
    path(
        "course/<int:course_id>/modules/<int:module_id>/",
        ModuleDetail.as_view(),
        name="course-module-detail",
    ),
]

assignmenturls = [
    path(
        "course/<int:course_id>/assignments/",
        Assignment.as_view(),
        name="course-assignment",
    ),
]

urlpatterns = [
    path("", Dashboard.as_view(), name="dashboard"),
]


# adding home to urlpattern
urlpatterns += homeurls

# adding syllabus to urlpattern
urlpatterns += syllabusurls

# adding people to urlpattern
urlpatterns += peopleurls

# adding announcement to urlpattern
urlpatterns += announcementurls

# adding module to urlpattern
urlpatterns += moduleurls

# adding assignment to urlpattern
urlpatterns += assignmenturls
