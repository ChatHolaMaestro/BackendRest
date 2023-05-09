from apps.shared.api import permissions
from apps.shared.api.views import GenericModelViewSet
from apps.schools.api.serializers import SchoolManagerSerializer


class SchoolManagerViewSet(GenericModelViewSet):
    """Provides functionality for managing school managers. Available actions:
    - list: Returns a list of school managers. Available for admins.
    - retrieve: Returns a school manager. Available for admins or if the user
    is the same as the requested school manager.
    - create: Creates a new school manager. Available for superusers. To register
    a new user the common way, use the `auth` endpoint.
    - update: Updates a school manager. Available for admins.
    - destroy: Deletes a school manager. Available for admins.
    """

    queryset = SchoolManagerSerializer.Meta.model.objects.all()
    serializer_class = SchoolManagerSerializer

    permission_classes = [permissions.IsAuthenticated]
    list_permission_classes = [permissions.IsAdminRole]
    retrieve_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsSameUser)
    ]
    create_permission_classes = [permissions.IsSuperUser]
    update_permission_classes = [permissions.IsAdminRole]
    destroy_permission_classes = [permissions.IsAdminRole]
