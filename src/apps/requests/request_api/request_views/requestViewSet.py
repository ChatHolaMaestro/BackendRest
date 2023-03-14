from django.shortcuts import render
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.requests.request_api.request_serializers.requestSerializer import (
    RequestViewSerializer,
    RequestCreationSerializer,
)
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class RequestViewSet(GenericModelViewSet):
    """
    Generic Request View Set
        - GET: list all requests
        - POST: create a request
        - GET(id): get a request by id
        - PUT(id): update a request by id
        - /search_teacher: GET(Teacher id): Get all requests by teacher id
        - /search_student: GET(Student id): Get all requests by student id
    """

    serializer_class = RequestViewSerializer
    serializer_create_class = RequestCreationSerializer
    serializer_update_class = RequestCreationSerializer

    @action(detail=False, methods=["get"])
    def search_teacher(self, request):
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

    @action(detail=False, methods=["get"])
    def search_student(self, request):
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
