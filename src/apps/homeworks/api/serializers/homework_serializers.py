from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.homeworks.models import Homework
from apps.requests.models import Request


class HomeworkSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Homework` model intended for list/retrieve actions.
    Provides the following fields:
        - id
        - status
        - topic
        - details
        - time_spent
        - scheduled_date
        - request (nested object)
    """

    request = serializers.RequestNestedSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Homework
        fields = (
            "id",
            "status",
            "topic",
            "details",
            "time_spent",
            "scheduled_date",
            "request",
        )


class WriteHomeworkSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Homework` model intended for create/update actions.
    Provides the following fields:
        - status
        - topic
        - details
        - time_spent
        - scheduled_date
        - request (id)
    """

    request = rf_serializers.PrimaryKeyRelatedField(
        queryset=Request.objects.all(), allow_null=True
    )

    class Meta:
        model = Homework
        fields = (
            "status",
            "topic",
            "details",
            "time_spent",
            "scheduled_date",
            "request",
        )
