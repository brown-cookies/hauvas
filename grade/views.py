from common.util.get_courses import get_courses
from common.util.views import View
from dashboard.models import Course
from django.shortcuts import get_list_or_404, get_object_or_404, render
from django.views.generic import TemplateView


# Create your views here.
class GradeList(View, TemplateView):
    template_name = "grade/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Grades"
        context["link"] = "grade"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        user = request.user

        courses = get_courses(user)

        context["courses"] = courses

        return render(request, self.template_name, context)


class GradeDetail(View, TemplateView):
    template_name = "grade/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Grades"
        context["link"] = "grade"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeCreate(View, TemplateView):
    template_name = "grade/create.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Grades"
        context["link"] = "grade"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeUpdate(View, TemplateView):
    template_name = "grade/update.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = "Grades"
        context["link"] = "grade"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeProfessorCourse(View, TemplateView):
    template_name = "grade/professor/course.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = get_object_or_404(Course, pk=course_id)
        enrollments = course.enrollments.all()

        context["title"] = f"{course.codename} Grades"
        context["link"] = "grade"

        context["course"] = course
        context["enrollments"] = enrollments

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)
