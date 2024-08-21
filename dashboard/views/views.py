from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import PermissionRequiredMixin

from common.util.views import View


class Dashboard(PermissionRequiredMixin, View, TemplateView):
    template_name = "dashboard/index.html"

    permission_required = ["dashboard.view_course"]
    permission_denied_message = "You're not allowed to view this course!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["link"] = "dashboard"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
