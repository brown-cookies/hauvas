from django.shortcuts import render, get_object_or_404

from dashboard.util.view import DashboardParentView
from dashboard.models import Course, ModuleItem
from common.util.get_modules import get_modules


class Module(DashboardParentView):
    template_name = "dashboard/module/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course: Course = context["course"]

        modules = get_modules(course.modules.all())

        context["title"] = f"{context['title']} Modules"
        context["sub_link"] = "module"
        context["modules"] = modules

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class ModuleDetail(DashboardParentView):
    template_name = "dashboard/module/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        module_id = kwargs.pop("module_id", None)

        module = get_object_or_404(ModuleItem, pk=module_id)

        context["title"] = f"{module.title}"
        context["link"] = "course"
        context["sub_link"] = "module"

        context["module"] = module

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
