from apps.shared.api import permissions
from apps.shared.api.views import GenericModelViewSet
from apps.schools.api.serializers import (
    SchoolManagerSerializer,
    WriteSchoolManagerSerializer,
)


class SchoolManagerViewSet(GenericModelViewSet):
    """Provides functionality for managing school managers. Available actions:
    - list: Returns a list of school managers.
    - retrieve: Returns a school manager.
    - create: Creates a new school manager. Available for admins. To register
    a new user the common way, use the `auth` endpoint.
    - update: Updates a school manager. Available for admins.
    - destroy: Deletes a school manager. Available for admins.
    """

    queryset = SchoolManagerSerializer.Meta.model.objects.all()
    serializer_class = SchoolManagerSerializer
    create_serializer_class = WriteSchoolManagerSerializer
    update_serializer_class = WriteSchoolManagerSerializer

    permission_classes = [permissions.IsAuthenticated]
    create_permission_classes = [permissions.IsAdminRole]
    update_permission_classes = [permissions.IsAdminRole]
    destroy_permission_classes = [permissions.IsAdminRole]
