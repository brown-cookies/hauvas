from django.http import HttpRequest
from django.core.exceptions import PermissionDenied

from dashboard.models import Course


def role_have_course_access(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        user = request.user

        course_id = kwargs.get("course_id", None)
        course = Course.objects.get(pk=course_id)

        if user.profile.is_professor:
            # Ensure the professor owns the course before allowing access
            if user.id != course.professor.user.id:
                raise PermissionDenied(
                    "You're not allowed to view courses belonging to other professors!"
                )
        else:
            # Check if the student is enrolled in the course
            is_student_enrolled = course.enrollments.filter(student__user=user).exists()

            if not is_student_enrolled:
                raise PermissionDenied("You're not enrolled in this course!")

        return view_func(request, *args, **kwargs)

    return wrapper
