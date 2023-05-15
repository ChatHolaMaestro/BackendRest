from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.teachers.api.serializers import (
    ScheduleSlotSerializer,
    WriteScheduleSlotSerializer,
)

User = get_user_model()


class ScheduleViewSet(GenericModelViewSet):
    """Provides functionality for managing schedule slots. Available actions:
    - list: Returns a list of schedule slots.
    - retrieve: Returns a schedule slot.
    - create: Creates a new schedule slot. Available for admins and teachers.
    Teachers can only create schedule slots for themselves.
    - update: Updates a schedule slot. Available for admins and teachers.
    Teachers can only update schedule slots of themselves.
    - destroy: Deletes a schedule slot. Available for admins and teachers.
    Teachers can only delete schedule slots of themselves.
    """

    queryset = ScheduleSlotSerializer.Meta.model.objects.all()
    serializer_class = ScheduleSlotSerializer
    create_serializer_class = WriteScheduleSlotSerializer
    update_serializer_class = WriteScheduleSlotSerializer

    permission_classes = [permissions.IsAuthenticated]
    create_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
    update_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
    destroy_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, permissions.IsTeacherRole)
    ]
