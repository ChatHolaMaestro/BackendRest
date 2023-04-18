from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    IsAuthenticated,
    IsAdminRole,
    IsSchoolManagerRole,
    OrPermission,
)
from apps.schools.api.serializers import (
    SchoolManagerViewSerializer,
    SchoolManagerCreationSerializer,
)


class SchoolManagerViewSet(GenericModelViewSet):
    """
    Generic Viewset for School Manager
        - GET: list all school managers
        - POST: create a school manager
        - GET(id): get a school manager by id
        - PUT(id): update a school manager by id
        - DELETE(id): delete a school manager by id
    """

    serializer_class = SchoolManagerViewSerializer
    create_serializer_class = SchoolManagerCreationSerializer
    update_serializer_class = SchoolManagerCreationSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [IsAdminRole]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsSchoolManagerRole)]
    create_permission_classes = [IsAdminRole]
    update_permission_classes = [OrPermission(IsAdminRole, IsSchoolManagerRole)]
    destroy_permission_classes = [IsAdminRole]
