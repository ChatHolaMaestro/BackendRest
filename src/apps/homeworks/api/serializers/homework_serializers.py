from rest_framework import serializers

from apps.shared.api.serializers import RequestSerializerShort
from apps.homeworks.models import Homework


class HomeworkViewSerializer(serializers.ModelSerializer):
    """
    Homework Serializer for view
        - id
        - status
        - topic
        - details
        - time_spent
        - scheduled_date
        - request (object)
    """

    request = RequestSerializerShort()

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


class HomeworkCreationSerializer(serializers.ModelSerializer):
    """
    Homework Serializer for creation
        - id
        - status
        - topic
        - details
        - time_spent
        - scheduled_date
        - request (id)
    """

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
