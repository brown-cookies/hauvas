from django.http import HttpRequest, HttpResponse
from django.shortcuts import HttpResponse, redirect
from django.core.exceptions import BadRequest, ObjectDoesNotExist, PermissionDenied
from django.contrib.auth.models import User, Group, Permission

from common.util.decorator_func.is_role_in_groups import is_role_in_group


def allowed_roles(roles=[]):
    def decorator(view_func):
        def wrapper(request: HttpRequest, *args, **kwargs):

            # TODO: Add logic for administering allowed roles
            if not len(roles):
                raise PermissionDenied("NO ROLES ARE ALLOWED!")

            user = request.user
            groups = user.groups.all()

            is_authorized = is_role_in_group(roles, groups)

            if not is_authorized:
                raise PermissionDenied("NO ROLES ARE ALLOWED!")

            return view_func(request, *args, **kwargs)

        return wrapper

    return decorator


def admin_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for admin only roles

        return view_func(request, *args, **kwargs)

    return wrapper


def professor_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for professor only roles

        return view_func(request, *args, **kwargs)

    return wrapper


def student_only(view_func):
    def wrapper(request: HttpRequest, *args, **kwargs):

        # TODO: Add logic for student only roles

        return view_func(request, *args, **kwargs)

    return wrapper
