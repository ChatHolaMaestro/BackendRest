from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.homeworks.api.serializers import (
    HomeworkViewSerializer,
    HomeworkCreationSerializer,
)


class HomeworkViewSet(GenericModelViewSet):
    """
    ViewSet for Homework model
        - GET: list all homeworks
        - POST: create a homework
        - GET(id): get a homework by id
        - PUT(id): update a homework by id
        - DELETE(id): delete a homework by id
    """

    queryset = HomeworkViewSerializer.Meta.model.objects.all()
    serializer_class = HomeworkViewSerializer
    create_serializer_class = HomeworkCreationSerializer
    update_serializer_class = HomeworkCreationSerializer

    permission_classes = [permissions.IsAuthenticated]
    list_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
    retrieve_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
    create_permission_classes = [permissions.IsAdminRole]
    update_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
    destroy_permission_classes = [permissions.IsAdminRole]
