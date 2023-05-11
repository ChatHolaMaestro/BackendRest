from django.utils.translation import gettext_lazy as _

from rest_framework import status, request
from rest_framework.response import Response

from apps.shared.api import permissions
from apps.shared.api.views import GenericModelViewSet
from apps.users.api.serializers import UserSerializer


class UserViewSet(GenericModelViewSet):
    """Provides functionality for managing users. Available actions:
    - list: Returns a list of users. Available for admins.
    - retrieve: Returns a user. Available for admins and if the user is the same
    as the requested user.
    - create: Creates a new user. Available for superusers. To register a new
    user the common way, use the `auth` endpoint.
    - update: Updates a user. Available for admins and if the user is the same
    as the requested user.
    - destroy: Deletes a user. Available for admins.
    """

    queryset = UserSerializer.Meta.model.objects.all()
    serializer_class = UserSerializer

    permission_classes = [permissions.IsAuthenticated]
    list_permission_classes = [permissions.IsAdminRole]
    retrieve_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsSameUser)
    ]
    create_permission_classes = [permissions.IsSuperUser]
    update_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsSameUser)
    ]
    destroy_permission_classes = [permissions.IsAdminRole]

    def update(self, request: request.Request, *args, **kwargs) -> Response:
        """Updates a user. Only superusers can update other superusers. Only
        superusers can update `password`, `is_superuser`, `is_staff`, `is_active`
        of other users. A user can't update its own `role`. If the user is not
        found, a 404 response is returned.

        Args:
            request (Request): request information

        Returns:
            Response: updated user or error message
        """
        instance = self.get_object()
        is_same_user = instance.pk == request.user.pk

        if instance.is_superuser and not request.user.is_superuser:
            return Response(
                {"error": _("Only superusers can update other superusers")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for field in ["password", "is_superuser", "is_staff", "is_active"]:
            if field in request.data:
                if not request.user.is_superuser:
                    return Response(
                        {
                            "error": _(
                                "Only superusers can update the '{}' field".format(
                                    field
                                )
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                elif is_same_user:
                    return Response(
                        {
                            "error": _(
                                "Superuser can't update its own '{}' field".format(
                                    field
                                )
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        if "role" in request.data and is_same_user:
            return Response(
                {"error": _("User can't update its own 'role' field")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().update(request, *args, **kwargs)

    def destroy(self, request: request.Request, *args, **kwargs) -> Response:
        """Deletes a user. Only superusers can delete other superusers. A user
        can't delete itself. If the user is not found, a 404 response is returned.

        Args:
            request (Request): request information

        Returns:
            Response: 200 if the user is deleted or error message
        """
        instance = self.get_object()

        if instance.is_superuser and not request.user.is_superuser:
            return Response(
                {"error": _("Only superusers can delete other superusers")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if instance.pk == request.user.pk:
            return Response(
                {"error": _("User can't delete itself")},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().destroy(request, *args, **kwargs)
