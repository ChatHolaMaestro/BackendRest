import datetime

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers

User = get_user_model()


class NewEventSerializer(rf_serializers.Serializer):
    """Serializer for creating a new event in Google Calendar. Provides the following fields:
    - user (read-only, nested object)
    - user_id (write-only, required)
    - summary
    - description
    - start
    - end
    """

    user = serializers.UserNestedSerializer(read_only=True, allow_null=True)
    user_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, required=True, source="user"
    )
    summary = rf_serializers.CharField(max_length=255, required=True)
    description = rf_serializers.CharField(max_length=255, required=False)
    start = rf_serializers.CharField(max_length=64, required=True)
    end = rf_serializers.CharField(max_length=64, required=True)

    def validate(self, data):
        """Validate the data for the serializer.
        Checks that the start date and end date are in the format
        YYYY-MM-DDThh:mm:ss
        """

        start = data.get("start")
        end = data.get("end")

        if start and end:
            try:
                datetime.datetime.fromisoformat(start)
            except ValueError:
                raise rf_serializers.ValidationError(
                    _("The start date must be in the format YYYY-MM-DDThh:mm:ss")
                )
            try:
                datetime.datetime.fromisoformat(end)
            except ValueError:
                raise rf_serializers.ValidationError(
                    _("The end date must be in the format YYYY-MM-DDThh:mm:ss")
                )

        return data
