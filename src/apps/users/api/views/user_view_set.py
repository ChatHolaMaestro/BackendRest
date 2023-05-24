from django.utils.translation import gettext_lazy as _

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
