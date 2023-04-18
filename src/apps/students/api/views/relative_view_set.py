from apps.shared.api.views import GenericModelViewSet
from apps.students.api.serializers import (
    RelativeViewSerializer,
    RelativeCreationSerializer,
)


class RelativeViewSet(GenericModelViewSet):
    """
    Generic ViewSet for Relative Model
        - GET: list all relatives
        - POST: create a relative
        - GET(id): get a relative by id
        - PUT(id): update a relative by id
        - DELETE(id): delete a relative by id
    """

    serializer_class = RelativeViewSerializer
    create_serializer_class = RelativeCreationSerializer
    update_serializer_class = RelativeCreationSerializer
