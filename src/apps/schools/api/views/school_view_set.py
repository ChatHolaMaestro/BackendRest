from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    IsAuthenticated,
    IsAdminRole,
    IsSchoolManagerRole,
    OrPermission,
)
from apps.schools.api.serializers import (
    SchoolSerializer,
)


class SchoolViewSet(GenericModelViewSet):
    """
    Generic Viewset for School
        - GET: list all schools
        - POST: create a school
        - GET(id): get a school by id
        - PUT(id): update a school by id
        - DELETE(id): delete a school by id
        - GET (name): search school by name
    """

    serializer_class = SchoolSerializer

    permission_classes = [IsAuthenticated]
    create_permission_classes = [IsAdminRole]
    update_permission_classes = [OrPermission(IsAdminRole, IsSchoolManagerRole)]
    destroy_permission_classes = [IsAdminRole]

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
