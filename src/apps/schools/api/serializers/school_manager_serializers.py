from django.contrib.auth import get_user_model

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.schools.models import School, SchoolManager

User = get_user_model()


class SchoolManagerSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `SchoolManager` model. Provides the following fields:
    - id (read-only)
    - user (read-only, `UserNestedSerializer`)
    - user_id (write-only)
    - school (read-only, `SchoolNestedSerializer`)
    - school_id (write-only)
    """

    user = serializers.UserNestedSerializer(read_only=True, allow_null=True)
    user_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        source="user",
    )
    school = serializers.SchoolNestedSerializer(read_only=True, allow_null=True)
    school_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        write_only=True,
        required=False,
        source="school",
    )

    class Meta:
        model = SchoolManager
        fields = ("id", "user", "user_id", "school", "school_id")
        extra_kwargs = {"id": {"read_only": True}}
