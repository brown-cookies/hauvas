from datetime import time
from django.contrib.auth.models import User


def get_courses(user: User):
    courses = None

    if user.profile.is_student:
        courses = get_student_courses(user)

    elif user.profile.is_professor:
        courses = get_professor_courses(user)

    return courses


def get_student_courses(user: User):
    student = user.student

    courses = []

    for enrollment in student.enrollments.all():
        course = enrollment.course

        time_from = course.start_time.strftime("%I:%M %p")
        time_to = course.end_time.strftime("%I:%M %p")

        course_content = {
            "enrollment_id": enrollment.id,
            "id": course.id,
            "title": course.title,
            "code": course.code,
            "codename": course.codename,
            "department": course.department.abbr,
            "block": course.block.name,
            "time": f"{time_from}-{time_to}",
            "days": course.days,
            "room": course.room,
            "semester": course.semester.__str__(),
        }

        courses.append(course_content)

    return courses


def get_professor_courses(user: User):
    professor = user.professor

    courses = []

    for course in professor.courses.all():

        time_from = course.start_time.strftime("%I:%M %p")
        time_to = course.end_time.strftime("%I:%M %p")

        course_content = {
            "id": course.id,
            "title": course.title,
            "code": course.code,
            "codename": course.codename,
            "department": course.department.abbr,
            "block": course.block.name,
            "time": f"{time_from}-{time_to}",
            "days": course.days,
            "room": course.room,
            "semester": course.semester.__str__(),
        }
        courses.append(course_content)
    return courses
