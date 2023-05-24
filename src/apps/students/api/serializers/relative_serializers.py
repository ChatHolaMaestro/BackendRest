from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.students.models import Relative, Student


class RelativeViewSerializer(serializers.NonNullModelSerializer):
    """
    Relative serializer:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - students (object)
    """

    # students = StudentViewSerializer(many=True, read_only=True)
    students = serializers.StudentSerializerShort(many=True, read_only=True)

    class Meta:
        model = Relative
        exclude = ["is_active", "created_date", "modified_date", "deleted_date"]


class RelativeCreationSerializer(serializers.NonNullModelSerializer):
    """
    Relative Serializer for creation:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - students (numbers)
    """

    students = rf_serializers.PrimaryKeyRelatedField(
        many=True, queryset=Student.objects.all(), required=False, write_only=True
    )

    class Meta:
        model = Relative
        exclude = ["is_active", "created_date", "modified_date", "deleted_date"]
