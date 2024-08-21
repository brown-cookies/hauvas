from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
from .forms import UserLoginForm
from main.forms import ProfileForm, ChangePasswordForm
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from dashboard.views.views import View


# Create your views here.
class LoginPageView(TemplateView):
    template_name = "pages/login.html"

    def get(self, request, *args, **kwargs):

        if request.user.is_authenticated:
            return redirect("dashboard:dashboard")

        form = UserLoginForm()
        context = {"form": form, "next": request.GET.get("next", None)}

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        form = UserLoginForm(data=request.POST)
        context = {"form": form, "next": request.GET.get("next")}

        if not form.is_valid():
            messages.error(request, "Invalid username or password.")
            return render(request, self.template_name, context)

        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        remember_me = form.cleaned_data["remember_me"]

        user = authenticate(username=username, password=password)

        if not user:
            messages.error(request, "Not a user")
            return render(request, self.template_name, context)

        login(request, user)

        # set session to expire when browser close (1 Month)
        if remember_me:
            request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            request.session.set_expiry(0)

        if context["next"]:
            return redirect(context["next"])

        return redirect("dashboard:dashboard")


class LogoutPageView(TemplateView):
    def get(self, request, *args, **kwargs):

        logout(request)
        return redirect("login")


class ProfilePageView(View, TemplateView):
    template_name = "pages/profile.html"

    def get(self, request, *args, **kwargs):
        form = ProfileForm()

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Profile"
        context["link"] = "profile"
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # TODO: Update profile data
        return redirect("profile")


class SecurityPageView(View, TemplateView):
    template_name = "pages/security.html"

    def get(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user)

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Security"
        context["link"] = "security"
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = ChangePasswordForm(self.request.user, data=request.POST)

        context = self.get_context_data(*args, **kwargs)

        context["title"] = "Security"
        context["link"] = "security"
        context["form"] = form

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password changed successfully.")
            return render(request, self.template_name, context)
        else:
            messages.error(request, "An error occurred when changing password.")
            return render(request, self.template_name, context)


""" 
========================================================================
# Custom Error Handler
========================================================================
"""


def custom_400_view(request, exception):
    context = {"exception": exception}

    return render(request, "400.html", context, status=400)


def custom_403_view(request, exception):
    context = {"exception": exception}

    return render(request, "403.html", context, status=403)


def custom_404_view(request, exception):
    context = {"exception": exception}

    return render(request, "404.html", context, status=404)


def custom_500_view(request):
    return render(request, "500.html", status=500)
