from announcement.models import Announcement
from django.core.paginator import Paginator
from django.shortcuts import render
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

        return render(request, self.template_name, context)
