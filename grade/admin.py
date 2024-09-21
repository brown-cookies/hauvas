from . import models
from django.contrib import admin

# Register your models here.
admin.site.register(models.Activity)
admin.site.register(models.Exam)
admin.site.register(models.StudentActivity)
admin.site.register(models.StudentExam)
