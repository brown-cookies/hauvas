from .forms.create import ComposeInboxForm
from .models import Inbox
from common.util.views import View
from enum import Enum
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import TemplateView
from main.models import Profile
from urllib.parse import urlencode


class InboxType(Enum):
    ALL = "all"
    SENT = "sent"
    STARRED = "starred"
    ARCHIVED = "archived"
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
        elif query_params["type"] == InboxType.ARCHIVED.value:
            inbox_list = self.get_inbox_list_archived(request, page)
        elif query_params["type"] == InboxType.TRASH.value:
            inbox_list = self.get_inbox_list_trash(request, page)
        else:
            return False

        return inbox_list

    def get_inbox_list_all(self, request, page, per_page=10):
        user = request.user
        inbox_list = (
            Inbox.objects.all()
            .filter(receiver=user)
            .filter(is_starred=False)
            .filter(is_trashed=False)
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

    def get_inbox_list_sent(self, request, page, per_page=10):
        user = request.user
        inbox_list = Inbox.objects.all().filter(sender=user).order_by("-created_at")

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

    def get_inbox_list_archived(self, request, page, per_page=10):
        user = request.user
        inbox_list = (
            Inbox.objects.all()
            .filter(receiver=user)
            .filter(is_archived=True)
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

    def get_inbox_list_trash(self, request, page, per_page=10):
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

        context["type"] = inbox_type
        context["inboxes"] = inboxes

        return render(request, self.template_name, context)


class InboxCompose(View, TemplateView):
    template_name = "inbox/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Compose"
        context["link"] = "inbox"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = ComposeInboxForm()

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        context = self.get_context_data(*args, **kwargs)

        form = ComposeInboxForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Error sending an inbox!")

        cleaned_receiver_email = form.cleaned_data.get("receiver")
        cleaned_subject = form.cleaned_data.get("subject")
        cleaned_content = form.cleaned_data.get("content")

        try:
            receiver_profile = Profile.objects.get(email=cleaned_receiver_email)
        except Profile.DoesNotExist:
            messages.error(request, "No existing user in the provided email address!")

        inbox_instance = Inbox()
        inbox_instance.receiver = receiver_profile.user
        inbox_instance.sender = request.user
        inbox_instance.subject = cleaned_subject
        inbox_instance.content = cleaned_content

        inbox_instance.save()
        messages.success(request, "Inbox sent successfully!")

        context["form"] = form
        context["form_success"] = True

        return render(request, self.template_name, context)


class InboxView(View, TemplateView):
    template_name = "inbox/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        inbox_id = kwargs.pop("inbox_id", None)

        inbox_instance = get_object_or_404(Inbox, pk=inbox_id)

        inbox_instance.is_read = True

        inbox_instance.save()

        context["title"] = inbox_instance.subject
        context["link"] = "inbox"
        context["inbox"] = inbox_instance
        context["sender_group"] = (
            "professor"
            if inbox_instance.sender.groups.filter(name="professor").exists()
            else "student"
        )

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)
        starred_success = bool(request.GET.get("starred_success", None))
        archived_success = bool(request.GET.get("archived_success", None))

        if starred_success:
            context["starred_success"] = True
        if archived_success:
            context["starred_success"] = True

        return render(request, self.template_name, context)


class InboxMarkAsStarred(View, TemplateView):
    def get(self, request, *args, **kwargs):
        inbox_id = kwargs.pop("inbox_id", None)

        inbox_instance = get_object_or_404(Inbox, pk=inbox_id)
        inbox_instance.is_starred = not inbox_instance.is_starred

        inbox_instance.save()

        url = reverse("inbox:inbox-view", kwargs={"inbox_id": inbox_id})

        query_params = {"starred_success": 1}

        return redirect(f"{url}?{urlencode(query_params)}")


class InboxMarkAsArchived(View, TemplateView):
    def get(self, request, *args, **kwargs):
        inbox_id = kwargs.pop("inbox_id", None)

        inbox_instance = get_object_or_404(Inbox, pk=inbox_id)
        inbox_instance.is_archived = not inbox_instance.is_archived

        inbox_instance.save()

        url = reverse("inbox:inbox-view", kwargs={"inbox_id": inbox_id})

        query_params = {"archived_success": 1}

        return redirect(f"{url}?{urlencode(query_params)}")


class InboxTrashed(View, TemplateView):
    pass
