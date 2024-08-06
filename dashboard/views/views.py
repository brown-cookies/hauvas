from django.shortcuts import render
from django.views.generic import TemplateView
from common.util.views import View


class Dashboard(View, TemplateView):
    template_name = "dashboard/index.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["link"] = "dashboard"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
