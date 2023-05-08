from rest_framework import status, request
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    OrPermission,
    IsAuthenticated,
    IsSuperUser,
    IsAdminRole,
    IsSameUser,
)
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
    - destroy: Deletes a user. Available for admins and if the user is the same
    as the requested user.
    """

    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [IsAdminRole]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsSameUser)]
    create_permission_classes = [IsSuperUser]
    update_permission_classes = [OrPermission(IsAdminRole, IsSameUser)]
    destroy_permission_classes = [IsAdminRole]

    def update(self, request: request.Request, *args, **kwargs) -> Response:
        """Updates a user. Only superusers can update other superusers. Only
        superusers can update `password`, `is_superuser`, `is_staff`, `is_active`
        of other users. A user can't update its own `role`. If the user is not
        found, a 404 response is returned.

        Args:
            request (Request): request information

        Returns:
            Response: 200 if the user is updated, 400 if invalid request, 404 if
            the user is not found
        """
        instance = self.get_object()
        is_same_user = instance.pk == request.user.pk

        if instance.is_superuser and not request.user.is_superuser:
            return Response(
                {"error": "Only superusers can update other superusers"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        for field in ["password", "is_superuser", "is_staff", "is_active"]:
            if field in request.data:
                if not request.user.is_superuser:
                    return Response(
                        {
                            "error": "Only superusers can update the '{}' field".format(
                                field
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
                elif is_same_user:
                    return Response(
                        {
                            "error": "Superuser can't update its own '{}' field".format(
                                field
                            )
                        },
                        status=status.HTTP_400_BAD_REQUEST,
                    )
        if "role" in request.data and is_same_user:
            return Response(
                {"error": "User can't update its own 'role' field"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().update(request, *args, **kwargs)

    def destroy(self, request: request.Request, *args, **kwargs) -> Response:
        """Deletes a user. Only superusers can delete other superusers. A user
        can't delete itself. If the user is not found, a 404 response is returned.

        Args:
            request (Request): request information

        Returns:
            Response: 200 if the user is deleted, 400 if invalid request, 404 if
            the user is not found
        """
        instance = self.get_object()

        if instance.is_superuser and not request.user.is_superuser:
            return Response(
                {"error": "Only superusers can delete other superusers"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        if instance.pk == request.user.pk:
            return Response(
                {"error": "User can't delete itself"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return super().destroy(request, *args, **kwargs)
