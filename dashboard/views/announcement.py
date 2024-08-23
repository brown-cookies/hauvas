from django.shortcuts import render
from django.contrib import messages

from dashboard.util.view import DashboardParentView
from dashboard.forms.announcement.create import CreateAnnouncementForm


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


class AnnouncementCreate(DashboardParentView):
    template_name = "dashboard/announcement/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Create an Announcement"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = CreateAnnouncementForm()

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = CreateAnnouncementForm(data=request.POST)
        course = context["course"]

        context["form"] = form

        if not form.is_valid():
            messages.error(request, "Invalid!")
            return render(request, self.template_name, context)

        announcement_instance = form.save(commit=False)
        announcement_instance.course = course

        announcement_instance.save()

        context["form_success"] = True

        messages.success(request, "Announcement Created!")
        return render(request, self.template_name, context)


class AnnouncementUpdate(DashboardParentView):
    template_name = "dashboard/announcement/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Update an Announcement"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
