from announcement.models import Announcement
from announcement.forms.create import CreateAnnouncementForm
from announcement.forms.update import UpdateAnnouncementForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from common.util.views import View
from django.views.generic import TemplateView


# Create your views here.
class AnnouncementList(View, TemplateView):
    template_name = "announcement/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Announcements"
        context["link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)
        page_number = request.GET.get("page", 1)
        announcements = Announcement.objects.all().order_by("-created_at")
        paginator = Paginator(announcements, 10)
        page_obj = paginator.get_page(page_number)

        context["page_obj"] = page_obj

        return render(request, self.template_name, context)


class AnnouncementDetail(View, TemplateView):
    template_name = "announcement/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Announcements"
        context["link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)
        announcement_id = kwargs.pop("announcement_id", None)

        announcement_instance = get_object_or_404(Announcement, pk=announcement_id)

        context["announcement"] = announcement_instance

        return render(request, self.template_name, context)


class AnnouncementCreate(View, TemplateView):
    template_name = "announcement/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Announcements"
        context["link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = CreateAnnouncementForm(user=request.user)

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = CreateAnnouncementForm(data=request.POST, user=request.user)

        if not form.is_valid():
            messages.error(request, "Invalid!")
            return render(request, self.template_name, context)

        context["form"] = form

        announcement = Announcement()
        announcement.course = form.cleaned_data["course"]
        announcement.title = form.cleaned_data["title"]
        announcement.short_description = form.cleaned_data["short_description"]
        announcement.content = form.cleaned_data["content"]

        announcement.save()

        context["form_success"] = True

        messages.success(request, "Announcement Created!")
        return render(request, self.template_name, context)


class AnnouncementUpdate(View, TemplateView):
    template_name = "announcement/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Announcements"
        context["link"] = "announcement"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = UpdateAnnouncementForm()

        announcement_id = kwargs.pop("announcement_id", None)
        announcement_instance = get_object_or_404(Announcement, pk=announcement_id)

        context["form"] = form
        context["announcement"] = announcement_instance

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = UpdateAnnouncementForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid!")
            return render(request, self.template_name, context)

        announcement_id = kwargs.pop("announcement_id", None)
        announcement_instance = get_object_or_404(Announcement, pk=announcement_id)

        announcement_instance.title = form.cleaned_data["title"]
        announcement_instance.short_description = form.cleaned_data["short_description"]
        announcement_instance.content = form.cleaned_data["content"]

        announcement_instance.save()

        context["form_success"] = True

        context["form"] = form
        context["announcement"] = announcement_instance

        messages.success(request, "Announcement Updated!")
        return render(request, self.template_name, context)
