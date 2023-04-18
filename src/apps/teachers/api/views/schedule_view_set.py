from apps.shared.api.views import GenericModelViewSet
from apps.teachers.api.serializers import (
    ScheduleViewSerializer,
    ScheduleCreationSerializer,
)


class ScheduleViewSet(GenericModelViewSet):
    """
    Generic viewset for schedule model
        - GET: list all schedules
        - POST: create a schedule
        - GET(id): get a schedule by id
        - PUT(id): update a schedule by id
        - DELETE(id): delete a schedule by id
    """

    serializer_class = ScheduleViewSerializer
    create_serializer_class = ScheduleCreationSerializer
    update_serializer_class = ScheduleCreationSerializer
