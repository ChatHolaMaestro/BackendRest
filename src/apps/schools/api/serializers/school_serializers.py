from rest_framework import serializers as rf_serializers


from apps.shared.api import serializers
from apps.schools.models import School


class SchoolSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `School` model. Provides the following fields:
    - id (read-only)
    - name
    - address
    - has_morning_hours
    - has_afternoon_hours
    - school_manager (read-only, nested list of objects)
    """

    school_managers = serializers.SchoolManagerOfSchoolNestedSerializer(
        read_only=True, many=True
    )

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
        read_only_fields = ("id",)
