from django.shortcuts import render
from django.contrib import messages
from dashboard.util.view import DashboardParentView
from dashboard.forms.syllabus.update import SyllabusUpdateForm


class Syllabus(DashboardParentView):
    template_name = "dashboard/syllabus/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Syllabus"
        context["sub_link"] = "syllabus"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class SyllabusUpdate(DashboardParentView):
    template_name = "dashboard/syllabus/update.html"

    permission_denied_message = (
        "You're not allowed to view and edit this course syllabus!"
    )

    def __init__(self):
        permissions = ["dashboard.change_about"]
        self.permission_required = self.override_permissions_required(
            permissions=permissions
        )

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"Update {context['title']} About"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        context["form"] = SyllabusUpdateForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = SyllabusUpdateForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid Syllabus content!")
            return render(request, self.template_name, context)

        course = context["course"]
        syllabus = form.cleaned_data["syllabus"]

        course.syllabus = syllabus

        course.save()

        context["form_success"] = True

        messages.success(request, "Syllabus content changed successfully!")
        return render(request, self.template_name, context)
