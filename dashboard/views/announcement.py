from common.util.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from dashboard.models import Course


class Announcement(View, TemplateView):
    template_name = "dashboard/announcement/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = Course.objects.get(pk=course_id)

        context["title"] = f"{course.title} Announcement"
        context["link"] = "course"
        context["sub_link"] = "announcement"

        context["course"] = course

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
