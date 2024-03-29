from rest_framework import permissions
from rest_framework.request import Request

from apps.users.models import User


class AllowAny(permissions.BasePermission):
    """
    Allow any access.
    """

    def has_permission(self, request: Request, view) -> bool:
        return True


class BasePermission(permissions.BasePermission):
    """
    Base permission class for all permissions.
    By default, if the request has a user that is authenticated and is a superuser,
    the permission is granted.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user and request.user.is_authenticated and request.user.is_superuser
        )


class IsSuperUser(BasePermission):
    """
    Allows access only to authenticated superusers.
    """


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request: Request, view) -> bool:
        return request.user and request.user.is_authenticated


class IsStaffUser(BasePermission):
    """
    Allows access only to staff users.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.is_staff
            or super().has_permission(request, view)
        )


class IsAdminRole(BasePermission):
    """
    Allows access only to users with the User.ADMIN role.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.ADMIN
            or super().has_permission(request, view)
        )


class IsTeacherRole(BasePermission):
    """
    Allows access only to users with the User.TEACHER role.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.TEACHER
            or super().has_permission(request, view)
        )


class IsSchoolManagerRole(BasePermission):
    """
    Allows access only to users with the User.SCHOOL_MANAGER role.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.SCHOOL_MANAGER
            or super().has_permission(request, view)
        )


class IsSameUser(BasePermission):
    """
    Allows access to resource only if user is the same as the one in the URL pk.
    """

    def has_permission(self, request: Request, view) -> bool:
        return (
            request.user
            and request.user.is_authenticated
            and request.user.id == request.parser_context["kwargs"]["pk"]
            or super().has_permission(request, view)
        )
