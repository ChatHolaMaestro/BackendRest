from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from apps.shared.api import permissions
from apps.calendar.api.serializers import NewEventSerializer
from apps.calendar import create_calendar_event


class NewEventView(GenericAPIView):
    """View to create a new event in Google Calendar."""

    serializer_class = NewEventSerializer
    permission_classes = [permissions.IsAdminRole]

    def post(self, request: request.Request) -> Response:
        """Creates a new event in Google Calendar.

        Args:
            request: request data.

        Returns:
            Response: new event.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # if valid, serializer has the data to call the create_calendar_event function
        data = serializer.validated_data.copy()
        if data.get("description") is None:
            data["description"] = "No description."
        data["attendees"] = [data.pop("user").email]

        create_calendar_event.delay(**data)

        return Response(
            {"detail": "New event created created succesfully"},
            status=status.HTTP_201_CREATED,
        )
