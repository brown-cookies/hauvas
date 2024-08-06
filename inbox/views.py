from common.util.views import View
from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.
class InboxList(View, TemplateView):
    template_name = "inbox/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Inbox"
        context["link"] = "inbox"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
