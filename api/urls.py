from django.urls import path, include
from rest_framework import routers
from canvas.serializer import UserViewSet
from main.serializer import DepartmentViewSet, ProfileViewSet
from event.serializer import EventViewSet
from inbox.serializer import InboxViewSet
from dashboard.serializer import (
    ProfessorViewSet,
    CourseViewSet,
    EnrollmentViewSet,
    StudentViewSet,
)
from announcement.serializer import AnnouncementViewSet
from todo.serializer import TodoViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"departments", DepartmentViewSet)
router.register(r"profiles", ProfileViewSet)
router.register(r"events", EventViewSet)
router.register(r"inboxes", InboxViewSet)
router.register(r"professors", ProfessorViewSet)
router.register(r"courses", CourseViewSet)
router.register(r"enrollments", EnrollmentViewSet)
router.register(r"students", StudentViewSet)
router.register(r"announcements", AnnouncementViewSet)
router.register(r"todos", TodoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
