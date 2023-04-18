from rest_framework import serializers

from apps.shared.api.serializers import (
    SchoolSerializerShort,
    UserSerializerShort,
)
from apps.schools.models import SchoolManager


class SchoolManagerViewSerializer(serializers.ModelSerializer):
    """
    School Manager serializer
        - id
        - school (object)
        - user (object)
    """

    school = SchoolSerializerShort()
    user = UserSerializerShort()

    class Meta:
        model = SchoolManager
        fields = ["id", "user", "school"]


class SchoolManagerCreationSerializer(serializers.ModelSerializer):
    """
    School Manager serializer
        - id
        - school (id)
        - user (id)
    """

    class Meta:
        model = SchoolManager
        fields = [
            "id",
            "user",
            "school",
        ]
