from rest_framework.permissions import BasePermission
from rest_framework.request import Request


class IsAuthenticated(BasePermission):
    """
    Allows access only to authenticated users.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_authenticated


class IsAdminUser(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_staff


class IsSuperUser(BasePermission):
    """
    Allows access only to superusers.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_superuser


class IsTeacher(BasePermission):
    """
    Allows access only to teachers or greater.
    """

    def has_permission(self, request: Request, _view: object) -> bool:
        return request.user and request.user.is_teacher or request.user.is_admin
