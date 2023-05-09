from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    OrPermission,
    IsAuthenticated,
    IsAdminRole,
    IsTeacherRole,
)
from apps.requests.api.serializers import (
    RequestViewSerializer,
    RequestCreationSerializer,
)


class RequestViewSet(GenericModelViewSet):
    """
    Generic Request View Set
        - GET: list all requests
        - POST: create a request
        - GET(id): get a request by id
        - PUT(id): update a request by id
        - /search_by_teacher: GET(Teacher id): Get all requests by teacher id
        - /search_by_student: GET(Student id): Get all requests by student id
    """

    queryset = RequestViewSerializer.Meta.model.objects.all()
    serializer_class = RequestViewSerializer
    create_serializer_class = RequestCreationSerializer
    update_serializer_class = RequestCreationSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    create_permission_classes = [IsAdminRole]
    update_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    destroy_permission_classes = [IsAdminRole]
    search_by_teacher_permission_classes = [OrPermission(IsAdminRole, IsTeacherRole)]
    search_by_student_permission_classes = [IsAdminRole]

    @action(detail=False, methods=["get"], name="search_by_teacher")
    def search_by_teacher(self, request):
        """
        Search request by teacher
        """
        teacher = request.query_params.get("teacher")
        if teacher:
            queryset = self.get_queryset().filter(teacher__id=teacher)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No request found"}, status=status.HTTP_400_BAD_REQUEST
        )

    @action(detail=False, methods=["get"], name="search_by_student")
    def search_by_student(self, request):
        """
        Search request by student
        """
        student = request.query_params.get("student")
        if student:
            queryset = self.get_queryset().filter(student__id=student)
            serializer = self.get_serializer(queryset, many=True)
            if serializer.data:
                return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"detail": "No request found"}, status=status.HTTP_400_BAD_REQUEST
        )
