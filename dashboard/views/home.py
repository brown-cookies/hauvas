from django.shortcuts import render

from dashboard.util.view import DashboardParentView

from dashboard.forms.home.update import HomeUpdateForm


class Home(DashboardParentView):
    template_name = "dashboard/home/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} Home"
        context["sub_link"] = "home"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class HomeUpdate(DashboardParentView):
    template_name = "dashboard/home/update.html"

    permission_denied_message = "You're not allowed to view and edit this course about!"

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

        context["form"] = HomeUpdateForm()

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = HomeUpdateForm(data=request.POST)

        if form.is_valid():
            print("The content is")
            print(form.cleaned_data["content"])
        else:
            print("Not valid!")

        return render(request, self.template_name, context)
