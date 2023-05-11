from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.shared.api.views import GenericModelViewSet
from apps.students.api.serializers import (
    RelativeViewSerializer,
    RelativeCreationSerializer,
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

    queryset = RelativeViewSerializer.Meta.model.objects.all()
    serializer_class = RelativeViewSerializer
    create_serializer_class = RelativeCreationSerializer
    update_serializer_class = RelativeCreationSerializer

    @action(detail=False, methods=["get"])
    def search_identification_number(self, request):
        """
        Search a relative by identification_number
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
            {"detail": "No relative found"}, status=status.HTTP_400_BAD_REQUEST
        )
