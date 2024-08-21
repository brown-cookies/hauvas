from django.shortcuts import render

from dashboard.models import Course

from dashboard.util.view import DashboardParentView


class PeopleList(DashboardParentView):
    template_name = "dashboard/people/list.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        context["title"] = f"{context['title']} People"
        context["sub_link"] = "people"

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        course: Course = context["course"]

        professor = course.professor.user
        students = []
        enrollments = course.enrollments.all()

        for enrollment in enrollments:
            students.append(enrollment.student.user)

        context["professor"] = professor
        context["students"] = students

        return render(request, self.template_name, context)
