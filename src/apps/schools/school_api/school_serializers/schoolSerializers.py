from rest_framework import serializers

from apps.shared.api.serializers import (
    SchoolSerializerShort,
    SchoolManagerSerializerShort,
    UserSerializerShort,
)
from apps.schools.school_models.schoolModels import School, SchoolManager


class SchoolSerializer(serializers.ModelSerializer):
    """
    School serializer for view
        - id
        - name
        - address
        - has_morning_hours
        - has_afternoon_hours
        - SchoolManagers (list)
    """

    school_managers = SchoolManagerSerializerShort(many=True, read_only=True)

    class Meta:
        model = School
        fields = (
            "id",
            "name",
            "address",
            "has_morning_hours",
            "has_afternoon_hours",
            "school_managers",
        )


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
