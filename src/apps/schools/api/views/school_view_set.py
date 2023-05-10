from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api import permissions
from apps.schools.api.serializers import (
    SchoolSerializer,
)

User = get_user_model()


class IsSchoolManagerOfSchool(permissions.BasePermission):
    """
    Allows access only to school managers of the school.
    """

    def has_permission(self, request, view):
        return (
            request.user
            and request.user.is_authenticated
            and request.user.role == User.SCHOOL_MANAGER
            and request.user.school
            and request.user.school.id == view.kwargs["pk"]
            or super().has_permission(request, view)
        )


class SchoolViewSet(GenericModelViewSet):
    """Provides functionality for managing schools. Available actions:
    - list: Returns a list of schools.
    - retrieve: Returns a school.
    - create: Creates a new school. Available for admins.
    - update: Updates a school. Available for admins and school managers of
    the school.
    - destroy: Deletes a school. Available for admins.
    """

    queryset = SchoolSerializer.Meta.model.objects.all()
    serializer_class = SchoolSerializer

    permission_classes = [permissions.IsAuthenticated]
    create_permission_classes = [permissions.IsAdminRole]
    update_permission_classes = [
        permissions.OrPermission(permissions.IsAdminRole, IsSchoolManagerOfSchool)
    ]
    destroy_permission_classes = [permissions.IsAdminRole]

    @action(detail=False, methods=["get"], name="search_by_name")
    def search_by_name(self, request):
        """
        Search school by name
        """
        name = request.query_params.get("name")
        if name:
            queryset = self.get_queryset().filter(name__icontains=name)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No school found"}, status=status.HTTP_400_BAD_REQUEST
        )
