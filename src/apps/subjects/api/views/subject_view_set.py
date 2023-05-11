from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.subjects.api.serializers import (
    SubjectSerializer,
)


class SubjectViewset(GenericModelViewSet):
    """Provides functionality for managing subjects. Available actions:
    - list: Returns a list of subjects. Available for any user.
    - retrieve: Returns a subject. Available for any user.
    - create: Creates a new subject. Available for admins.
    - update: Updates a subject. Available for admins.
    - destroy: Deletes a subject. Available for admins.
    """

    queryset = SubjectSerializer.Meta.model.objects.all()
    serializer_class = SubjectSerializer

    permission_classes = [permissions.IsAuthenticated]
    create_permission_classes = [permissions.IsAdminRole]
    update_permission_classes = [permissions.IsAdminRole]
    destroy_permission_classes = [permissions.IsAdminRole]
