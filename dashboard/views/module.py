from common.util.views import View
from django.views.generic import TemplateView
from django.shortcuts import render
from dashboard.models import Course, ModuleItem
from common.util.get_modules import get_modules


class Module(View, TemplateView):
    template_name = "dashboard/module/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = Course.objects.get(pk=course_id)

        modules = get_modules(course.modules.all())

        context["title"] = f"{course.title} Modules"
        context["link"] = "course"
        context["sub_link"] = "module"

        context["course"] = course
        context["modules"] = modules

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class ModuleDetail(View, TemplateView):
    template_name = "dashboard/module/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)
        module_id = kwargs.pop("module_id", None)

        course = Course.objects.get(pk=course_id)
        module = ModuleItem.objects.get(pk=module_id)

        context["title"] = f"{module.title}"
        context["link"] = "course"
        context["sub_link"] = "module"

        context["course"] = course
        context["module"] = module

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
