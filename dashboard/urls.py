from django.urls import path
from .views.announcement import (
    Announcement,
    AnnouncementDetail,
    AnnouncementCreate,
    AnnouncementUpdate,
)
from .views.views import Dashboard
from .views.home import Home, HomeUpdate
from .views.syllabus import Syllabus, SyllabusUpdate
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
    path(
        "course/<int:course_id>/syllabus/update/",
        SyllabusUpdate.as_view(),
        name="course-syllabus-update",
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
    path(
        "course/<int:course_id>/announcements/<int:announcement_id>/",
        AnnouncementDetail.as_view(),
        name="course-announcement-detail",
    ),
    path(
        "course/<int:course_id>/announcements/create/",
        AnnouncementCreate.as_view(),
        name="course-announcement-create",
    ),
    path(
        "course/<int:course_id>/announcements/<int:announcement_id>/update/",
        AnnouncementUpdate.as_view(),
        name="course-announcement-update",
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
