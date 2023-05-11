from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.teachers.api.serializers import ScheduleSlotSerializer

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

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Creates a schedule slot. Only admins and teachers can create a schedule
        slot. If the user is a teacher, the schedule slot to create MUST have the
        same teacher as the user.

        Args:
            request (Request): request information

        Returns:
            Response: created schedule slot or error message
        """
        if request.user.role == User.TEACHER and "teacher_id" in request.data:
            if request.user.teacher.id != request.data["teacher_id"]:
                return Response(
                    {"error": _("A teacher can only create its own schedule slots")},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        return super().create(request, *args, **kwargs)

    def update(self, request: Request, *args, **kwargs) -> Response:
        """Updates a schedule slot. Only admins and teachers can update a schedule
        slot. If the user is a teacher, the schedule slot to update MUST have the
        same teacher as the user.

        Args:
            request (Request): request information

        Returns:
            Response: updated schedule slot or error message
        """
        instance = self.get_object()
        if (
            request.user.role == User.TEACHER
            and instance.teacher.id != request.user.teacher.id
        ):
            return Response(
                {"error": _("A teacher can only update its own schedule slots")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().update(request, *args, **kwargs)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        """Deletes a schedule slot. Only admins and teachers can delete a schedule
        slot. If the user is a teacher, the schedule slot to delete MUST have the
        same teacher as the user.

        Args:
            request (Request): request information

        Returns:
            Response: deleted schedule slot or error message
        """
        instance = self.get_object()
        if (
            request.user.role == User.TEACHER
            and instance.teacher.id != request.user.teacher.id
        ):
            return Response(
                {"error": _("A teacher can only delete its own schedule slots")},
                status=status.HTTP_400_BAD_REQUEST,
            )
        return super().destroy(request, *args, **kwargs)
