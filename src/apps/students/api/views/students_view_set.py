from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from apps.shared.api.views import GenericModelViewSet
from apps.students.api.serializers import (
    StudentViewSerializer,
    StudentCreationSerializer,
)
from apps.students.api.serializers import (
    RelativeViewSerializer,
    RelativeCreationSerializer,
)


class StudentViewSet(GenericModelViewSet):
    """
    Generic ViewSet for Student Model
        - GET: list all students
        - POST: create a student
        - GET(id): get a student by id
        - PUT(id): update a student by id
        - DELETE(id): delete a student by id
        - search_identification_number(id_number): search a student by id_number
        - search_first_name(name): search a student by first name
    """

    serializer_class = StudentViewSerializer
    create_serializer_class = StudentCreationSerializer
    update_serializer_class = StudentCreationSerializer

    @action(detail=False, methods=["get"])
    def search_identification_number(self, request):
        """
        Search a student by identification_number
        """
        identification_number = request.query_params.get("identification_number")
        if identification_number:
            queryset = self.get_queryset().filter(
                identification_number__icontains=identification_number
            )
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No student found"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["get"])
    def search_name(self, request):
        """
        Search a student by name (first_name or last_name)
        """
        name = request.query_params.get("name")
        if name:
            queryset = self.get_queryset().filter(
                Q(first_name__icontains=name) | Q(last_name__icontains=name)
            )
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No student found"}, status=status.HTTP_400_BAD_REQUEST
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
