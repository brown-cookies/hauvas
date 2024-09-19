from common.util.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView
from todo.models import Todo


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

        todos = Todo.objects.filter(user=request.user).order_by("-created_at")

        context["todos"] = todos

        return render(request, self.template_name, context)
