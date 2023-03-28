from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from django.db.models import Q

from apps.shared.api.views import GenericModelViewSet
from apps.teachers.teacher_api.teacher_serializers.teacherSerializers import (
    TeacherViewSerializer,
    TeacherCreationSerializer,
)
from apps.teachers.teacher_api.teacher_serializers.scheduleSerializer import (
    ScheduleViewSerializer,
    ScheduleCreationSerializer,
)


class TeacherViewSet(GenericModelViewSet):
    """
    Generic viewset for teacher model
        - GET: list all teachers
        - POST: create a teacher
        - GET(id): get a teacher by id
        - PUT(id): update a teacher by id
        - DELETE(id): delete a teacher by id
        - /search_identification_number: GET (identification_number): search teacher by identification number
        - /search_name: GET (name): search teacher by name
        - /search_subject: GET (subject): search teacher by subject
        - /search_email: GET (email): search teacher by email
    """

    serializer_class = TeacherViewSerializer
    create_serializer_class = TeacherCreationSerializer
    update_serializer_class = TeacherCreationSerializer

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
