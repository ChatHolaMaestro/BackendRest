from rest_framework.permissions import BasePermission
from rest_framework.request import Request

from apps.users.models import User


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_authenticated


class IsStaffUser(BasePermission):
    """
    Allows access only to staff users.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_staff


class IsSuperUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_superuser


class IsAdminRole(BasePermission):
    """
    Allows access only to users with User.ADMIN role.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.role == User.ADMIN


class IsTeacherRole(BasePermission):
    """
    Allows access only to users with User.TEACHER or User.ADMIN role.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.role in (User.TEACHER, User.ADMIN)


class IsSchoolManagerRole(BasePermission):
    """
    Allows access only to users with User.SCHOOL_MANAGER or User.ADMIN role.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.role in (User.SCHOOL_MANAGER, User.ADMIN)


class IsSameUser(BasePermission):
    """
    Allows access to resource only if user is the same as the one in the URL.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return (
            request.user
            and request.user.id == request.parser_context["kwargs"]["pk"]
            or request.user.role == User.ADMIN
        )
