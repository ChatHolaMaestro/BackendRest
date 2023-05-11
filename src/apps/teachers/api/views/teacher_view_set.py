from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.teachers.api.serializers import TeacherSerializer, WriteTeacherSerializer

User = get_user_model()


class IsSameUserAsTeacher(permissions.BasePermission):
    """
    Allows access to the teacher object if the request user is a teacher
    and its teacher id is the same as the teacher id in the url.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.TEACHER
            and request.user.teacher
            and request.user.teacher.id == view.kwargs["pk"]
            or super().has_permission(request, view)
        )


class TeacherViewSet(GenericModelViewSet):
    """Provides functionality for managing teachers. Available actions:
    - list: Returns a list of teachers.
    - retrieve: Returns a teachers.
    - create: Creates a new teacher. Available for admins. To register
    a new user the common way, use the `auth` endpoint.
    - update: Updates a teacher. Available for admins.
    - destroy: Deletes a teacher. Available for admins.
    """

    queryset = TeacherSerializer.Meta.model.objects.all()
    serializer_class = TeacherSerializer
    create_serializer_class = WriteTeacherSerializer
    update_serializer_class = WriteTeacherSerializer

    permission_classes = [permissions.IsAuthenticated]
    create_permission_classes = [permissions.IsAdminRole]
    update_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, IsSameUserAsTeacher)
    ]
    destroy_permission_classes = [permissions.IsAdminRole]

    @action(detail=False, methods=["get"])
    def search_identification_number(self, request):
        """
        Search teacher by identification number
        """
        identification_number = request.query_params.get("identification_number")
        if identification_number:
            queryset = self.get_queryset().filter(
                user__identification_number__icontains=identification_number
            )
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No teacher found"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["get"])
    def search_name(self, request):
        """
        Search teacher by name (first_name or last_name)
        """
        name = request.query_params.get("name")
        if name:
            queryset = self.get_queryset().filter(
                Q(user__first_name__icontains=name) | Q(user__last_name__icontains=name)
            )
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No teacher found"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["get"])
    def search_subject(self, request):
        """
        Search teacher by subject
        """
        subject = request.query_params.get("subject")
        if subject:
            queryset = self.get_queryset().filter(subjects__name__icontains=subject)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No teacher found"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["get"])
    def search_email(self, request):
        """
        Search teacher by email
        """
        email = request.query_params.get("email")
        if email:
            queryset = self.get_queryset().filter(user__email__icontains=email)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No teacher found"}, status=status.HTTP_400_BAD_REQUEST
        )
