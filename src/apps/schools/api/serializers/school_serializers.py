from rest_framework import serializers

from apps.schools.models import School


class SchoolSerializer(serializers.ModelSerializer):
    """Serializer for the `School` model. Provides the following fields:
    - id (read-only)
    - name
    - address
    - has_morning_hours
    - has_afternoon_hours
    """

    class Meta:
        model = School
        fields = (
            "id",
            "name",
            "address",
            "has_morning_hours",
            "has_afternoon_hours",
        )
        read_only_fields = ("id",)
