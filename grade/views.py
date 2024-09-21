from .forms import AddActivityForm, AddExamForm
from .models import Activity, Exam, StudentActivity, StudentExam
from common.util.get_courses import get_courses
from common.util.views import View
from dashboard.models import Course
from django.contrib import messages
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
        activities = Activity.objects.filter(course=course).order_by("-created_at")
        exams = Exam.objects.filter(course=course).order_by("-created_at")
        enrollments = course.enrollments.all()

        context["title"] = f"{course.codename} Grades"
        context["link"] = "grade"

        context["course"] = course
        context["activities"] = activities
        context["exams"] = exams
        context["enrollments"] = enrollments

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeActivity(View, TemplateView):
    template_name = "grade/professor/activity.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)
        activity_id = kwargs.pop("activity_id", None)

        course = get_object_or_404(Course, pk=course_id)
        activity = get_object_or_404(Activity, pk=activity_id)

        context["title"] = f"{course.codename} {activity.name}"
        context["link"] = "grade"

        context["course"] = course
        context["activity"] = activity

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeExam(View, TemplateView):
    template_name = "grade/professor/exam.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)
        exam_id = kwargs.pop("exam_id", None)

        course = get_object_or_404(Course, pk=course_id)
        exam = get_object_or_404(Activity, pk=exam_id)

        context["title"] = f"{course.codename} {exam.name}"
        context["link"] = "grade"

        context["course"] = course
        context["exam"] = exam

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeAddActivity(View, TemplateView):
    template_name = "grade/professor/add-activity.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = get_object_or_404(Course, pk=course_id)

        context["title"] = f"{course.codename} Add Activity"
        context["link"] = "grade"

        context["course"] = course

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddActivityForm()

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddActivityForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid Input!")

        activity_instance = form.save(commit=False)
        activity_instance.course = context["course"]

        activity_instance.save()

        enrollments = context["course"].enrollments.all()

        for enrollment in enrollments:
            student = enrollment.student

            student_activity = StudentActivity()
            student_activity.activity = activity_instance
            student_activity.student = student
            student_activity.score = 0

            student_activity.save()

        messages.success(request, "Success adding new activity!")

        context["form"] = form
        context["form_success"] = True

        return render(request, self.template_name, context)


class GradeAddExam(View, TemplateView):
    template_name = "grade/professor/add-exam.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = get_object_or_404(Course, pk=course_id)

        context["title"] = f"{course.codename} Add Exam"
        context["link"] = "grade"

        context["course"] = course

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddExamForm()

        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        form = AddExamForm(data=request.POST)

        if not form.is_valid():
            messages.error(request, "Invalid Input!")

        exam_instance = form.save(commit=False)
        exam_instance.course = context["course"]

        exam_instance.save()

        enrollments = context["course"].enrollments.all()

        for enrollment in enrollments:
            student = enrollment.student

            student_exam = StudentExam()
            student_exam.exam = exam_instance
            student_exam.student = student
            student_exam.score = 0

            student_exam.save()

        messages.success(request, "Success adding new exam!")

        context["form"] = form
        context["form_success"] = True

        return render(request, self.template_name, context)
