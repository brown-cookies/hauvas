from .forms import AddActivityForm, AddExamForm, StudentActivityForm, StudentExamForm
from .models import Activity, Exam, StudentActivity, StudentExam
from common.util.calculate_raw_score import calculate_raw_score
from common.util.determine_grade import determine_numeric_grade
from common.util.get_courses import get_courses
from common.util.transmute_raw_score import transmute_raw_score
from common.util.views import View
from dashboard.models import Course, Student
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

        course = context["course"]
        activity = context["activity"]
        enrollments = course.enrollments.all()
        students = []

        for enrollment in enrollments:
            student = enrollment.student
            student_activity = StudentActivity.objects.get(
                student=student, activity=activity
            )

            students.append(student_activity)

        context["enrollments"] = enrollments
        context["students"] = students

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeUpdateActivityScore(GradeActivity):
    template_name = "grade/professor/update-activity-score.html"

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        student_id = kwargs.pop("student_id", None)
        student = Student.objects.get(pk=student_id)

        form = StudentActivityForm()

        context["student"] = student
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        student_id = kwargs.pop("student_id", None)
        student = Student.objects.get(pk=student_id)

        form = StudentActivityForm(data=request.POST)
        activity = context["activity"]

        if not form.is_valid():
            messages.error(request, "Invalid Input!")

        student_activity_instance = StudentActivity.objects.get(
            student=student, activity=activity
        )

        student_activity_instance.score = form.cleaned_data["score"]

        student_activity_instance.save()

        messages.success(request, "Score successfully updated!")

        context["form"] = form
        context["form_success"] = True

        return render(request, self.template_name, context)


class GradeExam(View, TemplateView):
    template_name = "grade/professor/exam.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)
        exam_id = kwargs.pop("exam_id", None)

        course = get_object_or_404(Course, pk=course_id)
        exam = get_object_or_404(Exam, pk=exam_id)

        context["title"] = f"{course.codename} {exam.name}"
        context["link"] = "grade"

        context["course"] = course
        context["exam"] = exam

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        course = context["course"]
        exam = context["exam"]
        enrollments = course.enrollments.all()
        students = []

        for enrollment in enrollments:
            student = enrollment.student
            student_exam = StudentExam.objects.get(student=student, exam=exam)

            print(student_exam)

            students.append(student_exam)

        context["enrollments"] = enrollments
        context["students"] = students

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        return render(request, self.template_name, context)


class GradeUpdateExamScore(GradeExam):
    template_name = "grade/professor/update-exam-score.html"

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        student_id = kwargs.pop("student_id", None)
        student = Student.objects.get(pk=student_id)

        form = StudentExamForm()

        context["student"] = student
        context["form"] = form

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        student_id = kwargs.pop("student_id", None)
        student = Student.objects.get(pk=student_id)

        form = StudentActivityForm(data=request.POST)
        exam = context["exam"]

        if not form.is_valid():
            messages.error(request, "Invalid Input!")

        student_exam_instance = StudentExam.objects.get(student=student, exam=exam)

        student_exam_instance.score = form.cleaned_data["score"]

        student_exam_instance.save()

        messages.success(request, "Score successfully updated!")

        context["form"] = form
        context["form_success"] = True

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


class GradeStudentCourse(View, TemplateView):
    template_name = "grade/student/course.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        course_id = kwargs.pop("course_id", None)

        course = get_object_or_404(Course, pk=course_id)
        activities = Activity.objects.filter(course=course).order_by("-created_at")
        exams = Exam.objects.filter(course=course).order_by("-created_at")

        context["title"] = f"{course.codename} Grades"
        context["link"] = "grade"

        context["course"] = course
        context["activities"] = activities
        context["exams"] = exams

        return context

    def get(self, request, *args, **kwargs):

        context = self.get_context_data(*args, **kwargs)

        student = request.user.student
        activities = []
        exams = []

        for activity in context["activities"]:
            activities.append(activity.list.get(student=student))

        for exam in context["exams"]:
            exams.append(exam.list.get(student=student))

        raw_score = calculate_raw_score(request, context)
        transmute_score = transmute_raw_score(raw_score)
        numeric_grade = determine_numeric_grade(transmute_score)

        context["student_activities"] = activities
        context["student_exams"] = exams

        context["raw_score"] = raw_score
        context["transmute_score"] = transmute_score
        context["numeric_grade"] = numeric_grade

        return render(request, self.template_name, context)
