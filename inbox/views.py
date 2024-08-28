from urllib.parse import urlencode
from enum import Enum
from common.util.views import View
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView


class InboxType(Enum):
    ALL = "all"
    SENT = "sent"
    STARRED = "starred"
    TRASH = "trash"


# Create your views here.
class InboxList(View, TemplateView):
    template_name = "inbox/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Inbox"
        context["link"] = "inbox"

        return context

    def get_inbox_query_params(self, request):
        query_params = {}

        try:
            query_params["type"] = request.GET["type"]
            query_params["page"] = request.GET["page"]
        except:
            return None

        return query_params

    def get_inbox_list(self, request, query_params):
        inbox_list = []
        page = query_params["page"]

        if query_params["type"] == InboxType.ALL:
            inbox_list = self.get_inbox_list_all(request, page)
        elif query_params["type"] == InboxType.SENT:
            inbox_list = self.get_inbox_list_sent(request, page)
        elif query_params["type"] == InboxType.STARRED:
            inbox_list = self.get_inbox_list_starred(request, page)
        elif query_params["type"] == InboxType.TRASH:
            inbox_list = self.get_inbox_list_trash(request, page)
        else:
            return False

        return inbox_list

    def get_inbox_list_all(self, request, page):
        return True

    def get_inbox_list_sent(self, request, page):
        return True

    def get_inbox_list_starred(self, request, page):
        return True

    def get_inbox_list_trash(self, request, page):
        return True

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        default_query_params = {"type": "all", "page": 1}

        query_params = self.get_inbox_query_params(request)

        print("Default query params", default_query_params)
        print("Query params", query_params["type"])

        if query_params is None:
            return redirect(
                reverse("inbox:inbox") + f"?{urlencode(default_query_params)}"
            )

        inbox_list = self.get_inbox_list(request, query_params)

        context["type"] = query_params["type"]
        context["page"] = int(query_params["page"])
        context["page_from"] = (int(query_params["page"]) * 10) - 9
        context["page_to"] = int(query_params["page"]) * 10
        context["inboxes"] = inbox_list

        return render(request, self.template_name, context)


class InboxCompose(View, TemplateView):
    template_name = "inbox/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Compose"
        context["link"] = "inbox"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
