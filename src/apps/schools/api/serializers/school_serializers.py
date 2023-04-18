from rest_framework import serializers

from apps.shared.api.serializers import SchoolManagerSerializerShort
from apps.schools.models import School


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
