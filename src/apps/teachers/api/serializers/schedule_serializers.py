from rest_framework import serializers as rf_serializers

from rest_framework import serializers

from apps.shared.api import serializers
from apps.teachers.models import Teacher, ScheduleSlot


class ScheduleSlotSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `ScheduleSlot` model. Provides the following fields:
    - id (read-only)
    - day_of_week
    - start_time
    - end_time
    - request_type
    - teacher (read-only, nested object)
    - teacher_id (write-only)
    """

    teacher = serializers.TeacherOfScheduleSlotNestedSerializer(
        read_only=True, allow_null=True
    )
    teacher_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(),
        write_only=True,
        required=True,
        source="teacher",
    )

    class Meta:
        model = ScheduleSlot
        fields = (
            "id",
            "day_of_week",
            "start_time",
            "end_time",
            "request_type",
            "teacher",
            "teacher_id",
        )
        extra_kwargs = {"id": {"read_only": True}}
