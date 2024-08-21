from django.shortcuts import render

from dashboard.util.view import DashboardParentView


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
        permissions = ["dashboard.change_syllabus"]
        self.permission_required = self.override_permissions_required(
            permissions=permissions
        )
