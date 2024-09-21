from django.db import models


# Create your models here.
class Activity(models.Model):
    course = models.ForeignKey(
        "dashboard.Course", on_delete=models.CASCADE, related_name="activities"
    )
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.codename} Activity - {self.name} up to {self.score}"


class Exam(models.Model):
    course = models.ForeignKey(
        "dashboard.Course", on_delete=models.CASCADE, related_name="exams"
    )
    name = models.CharField(max_length=50)
    score = models.PositiveIntegerField(default=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.course.codename} Exam - {self.name} up to {self.score}"


class StudentActivity(models.Model):
    activity = models.ForeignKey(
        Activity, on_delete=models.CASCADE, related_name="list"
    )
    student = models.ForeignKey(
        "dashboard.Student", on_delete=models.CASCADE, related_name="activities"
    )
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudentExam(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, related_name="list")
    student = models.ForeignKey(
        "dashboard.Student", on_delete=models.CASCADE, related_name="exams"
    )
    score = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
