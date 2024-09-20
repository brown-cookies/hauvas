from .forms import AddEventForm
from .models import Event
from common.util.views import View
from datetime import datetime
from django.contrib import messages
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import TemplateView


# Create your views here.
class EventList(View, TemplateView):
    template_name = "event/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Events"
        context["link"] = "event"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        events = []

        event_list = get_list_or_404(Event, user=request.user)

        for event in event_list:
            e = {}
            e["id"] = event.id
            e["title"] = event.title
            e["description"] = event.description

            date_str = f"{event.start_date} {event.start_time}"

            input_format = "%Y-%m-%d %H:%M:%S"

            date_obj = datetime.strptime(date_str, input_format)

            formatted_date = date_obj.strftime("%Y-%m-%dT%H:%M:%S")

            e["start"] = formatted_date

            date_str = f"{event.end_date} {event.end_time}"

            input_format = "%Y-%m-%d %H:%M:%S"

            date_obj = datetime.strptime(date_str, input_format)

            formatted_date = date_obj.strftime("%Y-%m-%dT%H:%M:%S")

            e["end"] = formatted_date

            events.append(e)

        context["events"] = events

        return render(request, self.template_name, context)


class EventDetail(View, TemplateView):
    template_name = "event/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Events"
        context["link"] = "event"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        event_id = kwargs.pop("event_id", None)

        event = get_object_or_404(Event, pk=event_id)

        context["event"] = event

        return render(request, self.template_name, context)


class EventCreate(View, TemplateView):
    template_name = "event/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Events"
        context["link"] = "event"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddEventForm()

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddEventForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid Input!")

        event_instance = form.save(commit=False)
        event_instance.user = request.user

        event_instance.save()

        messages.success(request, "Event Created!")

        context["form"] = form
        context["form_success"] = True

        return render(request, self.template_name, context)


class EventUpdate(View, TemplateView):
    template_name = "event/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Events"
        context["link"] = "event"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
