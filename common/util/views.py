from django.contrib.auth.mixins import LoginRequiredMixin
from common.util.get_courses import get_courses


class View(LoginRequiredMixin):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)

        user = self.request.user
        session = self.request.session
        session_course_key = f"{user.id}-courses"

        if session_course_key in session:
            context["courses"] = session.get(session_course_key)
        else:
            courses = get_courses(user)

            session[session_course_key] = courses

            context["courses"] = courses

        return context
