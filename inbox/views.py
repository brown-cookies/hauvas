from .models import Inbox
from common.util.views import View
from enum import Enum
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from urllib.parse import urlencode


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

    def get_default_inbox_query_params(self):
        query_params = {"type": "all", "page": 1}

        return query_params

    def get_inbox_list(self, request, query_params):
        inbox_list = []
        page = query_params["page"]

        if query_params["type"] == InboxType.ALL.value:
            inbox_list = self.get_inbox_list_all(request, page)
        elif query_params["type"] == InboxType.SENT.value:
            inbox_list = self.get_inbox_list_sent(request, page)
        elif query_params["type"] == InboxType.STARRED.value:
            inbox_list = self.get_inbox_list_starred(request, page)
        elif query_params["type"] == InboxType.TRASH.value:
            inbox_list = self.get_inbox_list_trash(request, page)
        else:
            return False

        return inbox_list

    def get_inbox_list_all(self, request, page, per_page=10):
        user = request.user
        inbox_list = Inbox.objects.all().filter(receiver=user).order_by("-created_at")

        paginator = Paginator(inbox_list, per_page)
        try:
            paginated_items = paginator.page(page)
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        return paginated_items

    def get_inbox_list_sent(self, request, page, per_page=10):
        user = request.user
        inbox_list = Inbox.objects.all().filter(sent=user).order_by("-created_at")

        paginator = Paginator(inbox_list, per_page)
        try:
            paginated_items = paginator.page(page)
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        return paginated_items

    def get_inbox_list_starred(self, request, page, per_page=10):
        user = request.user
        inbox_list = (
            Inbox.objects.all()
            .filter(receiver=user)
            .filter(is_starred=True)
            .order_by("-created_at")
        )

        paginator = Paginator(inbox_list, per_page)
        try:
            paginated_items = paginator.page(page)
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        return paginated_items

    def get_inbox_list_trash(self, request, page, per_page):
        user = request.user
        inbox_list = (
            Inbox.objects.all()
            .filter(receiver=user)
            .filter(is_trashed=True)
            .order_by("-created_at")
        )

        paginator = Paginator(inbox_list, per_page)
        try:
            paginated_items = paginator.page(page)
        except PageNotAnInteger:
            paginated_items = paginator.page(1)
        except EmptyPage:
            paginated_items = paginator.page(paginator.num_pages)

        return paginated_items

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        inbox_type = request.GET.get("type") or None
        page = request.GET.get("page") or 1

        if inbox_type is None:
            url = reverse("inbox:inbox")
            query_params = urlencode(self.get_default_inbox_query_params())

            return redirect(f"{url}?{query_params}")

        query_params = {"type": inbox_type, "page": page}

        inboxes = self.get_inbox_list(request, query_params)

        context["inboxes"] = inboxes

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
