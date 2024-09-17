from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.core.paginator import Paginator

from dashboard.util.view import DashboardParentView
from dashboard.forms.announcement.create import CreateAnnouncementForm
from dashboard.forms.announcement.update import UpdateAnnouncementForm

from announcement.models import Announcement as AnnouncementModel


class Announcement(DashboardParentView):
    template_name = "dashboard/announcement/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Announcements"
        context["sub_link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)
        course = context["course"]
        page_number = request.GET.get("page", 1)
        announcements = course.announcements.all().order_by("-created_at")
        paginator = Paginator(announcements, 10)
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj

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
        announcement_id = kwargs.pop("announcement_id", None)

        announcement_instance = get_object_or_404(AnnouncementModel, pk=announcement_id)

        context["announcement"] = announcement_instance

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

        if not form.is_valid():
            messages.error(request, "Invalid!")
            return render(request, self.template_name, context)

        course = context["course"]

        context["form"] = form

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

        form = UpdateAnnouncementForm()

        announcement_id = kwargs.pop("announcement_id", None)
        announcement_instance = get_object_or_404(AnnouncementModel, pk=announcement_id)

        context["form"] = form
        context["announcement"] = announcement_instance

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = UpdateAnnouncementForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid!")
            return render(request, self.template_name, context)

        course = context["course"]

        announcement_id = kwargs.pop("announcement_id", None)
        announcement_instance = get_object_or_404(AnnouncementModel, pk=announcement_id)

        announcement_instance.title = form.cleaned_data["title"]
        announcement_instance.short_description = form.cleaned_data["short_description"]
        announcement_instance.content = form.cleaned_data["content"]

        announcement_instance.save()

        context["form_success"] = True

        context["form"] = form
        context["announcement"] = announcement_instance

        messages.success(request, "Announcement Updated!")
        return render(request, self.template_name, context)
