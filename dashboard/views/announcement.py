from django.shortcuts import render

from dashboard.util.view import DashboardParentView


class Announcement(DashboardParentView):
    template_name = "dashboard/announcement/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Announcements"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class AnnouncementDetail(DashboardParentView):
    template_name = "dashboard/announcement/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Announcements"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)