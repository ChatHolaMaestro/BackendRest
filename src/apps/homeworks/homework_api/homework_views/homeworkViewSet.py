from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    OrPermission,
    IsAuthenticated,
    IsAdminRole,
    IsTeacherRole,
)
from apps.homeworks.homework_api.homework_serializers.homeworkSerializer import (
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

    serializer_class = HomeworkViewSerializer
    create_serializer_class = HomeworkCreationSerializer
    update_serializer_class = HomeworkCreationSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    create_permission_classes = [IsAdminRole]
    update_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    destroy_permission_classes = [IsAdminRole]
