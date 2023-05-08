from typing import Iterable

from rest_framework.request import Request

from .shared_permissions import BasePermission


class OrPermission(BasePermission):
    """A permission that is true if any of its component permissions are true."""

    def __init__(self, *permissions: tuple[BasePermission]):
        self.permissions = permissions

    def get_permissions(self) -> Iterable[BasePermission]:
        return [permission() for permission in self.permissions]

    def has_permission(self, request: Request, view) -> bool:
        return any(
            permission.has_permission(request, view)
            for permission in self.get_permissions()
        )
