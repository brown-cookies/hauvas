from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views


# Custom 400.html BAD REQUEST handler
handler400 = views.custom_400_view

# Custom 403.html PERMISSION DENIED handler
handler403 = views.custom_403_view

# Custom 404.html PAGE NOT FOUND handler
handler404 = views.custom_404_view

# Custom 500.html SERVER ERROR handler
handler500 = views.custom_500_view


urlpatterns = [
    path("", include("dashboard.urls")),
    path("grappelli/", include("grappelli.urls")),
    path("admin/", admin.site.urls),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("logout/", views.LogoutPageView.as_view(), name="logout"),
    path("profile/", views.ProfilePageView.as_view(), name="profile"),
    path("security/", views.SecurityPageView.as_view(), name="security"),
    path("api-auth/", include("rest_framework.urls"), name="rest_framework"),
    path("announcements/", include("announcement.urls")),
    path("grades/", include("grade.urls")),
    path("inbox/", include("inbox.urls")),
    path("event/", include("event.urls")),
    path("todo/", include("todo.urls")),
    path("api/", include("api.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
