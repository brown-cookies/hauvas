from django.db import models
from django.conf import settings


# Create your models here.
class Student(models.Model):
    ACADEMIC_STATUS_CHOICES = [
        ("Active", "Active"),
        ("On leave", "On leave"),
        ("Suspended", "Suspended"),
        ("Excused", "Excused"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="student"
    )
    block = models.ForeignKey(
        "main.Block", on_delete=models.CASCADE, related_name="students"
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="students",
    )
    major = models.CharField(max_length=254)
    year = models.IntegerField()
    academic_status = models.CharField(
        max_length=254, choices=ACADEMIC_STATUS_CHOICES, default="Active"
    )
    is_graduated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"


class Professor(models.Model):
    ACADEMIC_RANK_CHOICES = [
        ("Professor", "Professor"),
        ("Assistant Professor", "Assistant Professor"),
        ("Associate Professor", "Associate Professor"),
        ("Full Professor", "Full Professor"),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="professor",
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="professors",
    )
    hire_date = models.DateTimeField()
    academic_rank = models.CharField(
        max_length=254, choices=ACADEMIC_RANK_CHOICES, default="Professor"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - {self.department.name}"


class Course(models.Model):
    DAYS_CHOICES = [
        ("MTH", "Monday and Thursday"),
        ("TF", "Tuesday and Friday"),
        ("WS", "Wednesday and Saturday"),
        ("M", "Monday"),
        ("T", "Tuesday"),
        ("W", "Wednesday"),
        ("TH", "Thursday"),
        ("F", "Friday"),
        ("S", "Saturday"),
        ("D", "Default"),
    ]

    professor = models.ForeignKey(
        Professor, on_delete=models.CASCADE, related_name="courses"
    )
    block = models.ForeignKey(
        "main.Block", on_delete=models.CASCADE, related_name="courses"
    )
    department = models.ForeignKey(
        "main.Department",
        on_delete=models.CASCADE,
        related_name="department",
    )
    semester = models.ForeignKey(
        "main.Semester", on_delete=models.CASCADE, related_name="semester"
    )
    title = models.CharField(max_length=254)
    code = models.CharField(max_length=6)
    codename = models.CharField(max_length=20)
    about = models.TextField(default="This is about course, populate it later")
    syllabus = models.TextField(default="This is syllabus course, populate it later")
    unit = models.IntegerField()
    start_time = models.TimeField(blank=True)
    end_time = models.TimeField(blank=True)
    days = models.CharField(max_length=20, choices=DAYS_CHOICES, default="D")
    room = models.CharField(max_length=20, default="undecided")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.professor.user.profile.first_name} | {self.code}:{self.codename} - {self.title}"


class Enrollment(models.Model):
    STATUS_CHOICES = [
        ("Enrolled", "Enrolled"),
        ("Withdrawn", "Withdrawn"),
        ("Dropped", "Dropped"),
    ]

    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    semester = models.ForeignKey(
        "main.Semester",
        on_delete=models.CASCADE,
        related_name="enrollments",
    )
    enrollment_date = models.DateTimeField()
    completion_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ModuleList(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="modules")
    title = models.CharField(max_length=254, default="Week-")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.title} | Module List {self.title}"


class ModuleItem(models.Model):
    module_list = models.ForeignKey(
        ModuleList, on_delete=models.CASCADE, related_name="items"
    )
    title = models.CharField(max_length=254, default="Lesson 01")
    short_description = models.CharField(
        max_length=254, default="Learn the {your explanation about the course}!"
    )
    description = models.TextField(
        default="Put your description here about the module, and even content"
    )
    content_url = models.CharField(max_length=255, default="none")
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.module_list.title} | Module {self.title}"
