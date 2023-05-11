from django.contrib.auth import get_user_model

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.schools.models import School, SchoolManager

User = get_user_model()


class SchoolManagerSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `SchoolManager` model intended for list/retrieve actions.
    Provides the following fields:
    - id
    - user (nested object)
    - school (nested object)
    """

    user = serializers.UserNestedSerializer(read_only=True, allow_null=True)
    school = serializers.SchoolNestedSerializer(read_only=True, allow_null=True)

    class Meta:
        model = SchoolManager
        fields = ("id", "user", "school")
        extra_kwargs = {"id": {"read_only": True}}


class WriteSchoolManagerSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `SchoolManager` model intended for create/write actions.
    Provides the following fields:
    - user (id)
    - school (id)
    """

    user = rf_serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
    )
    school = rf_serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        write_only=True,
        required=False,
    )

    class Meta:
        model = SchoolManager
        fields = ("user", "school")
