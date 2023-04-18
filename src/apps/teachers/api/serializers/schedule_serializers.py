from rest_framework import serializers

from apps.teachers.models import Schedule
from apps.shared.api.serializers import TeacherSerializerShort


class ScheduleViewSerializer(serializers.ModelSerializer):
    """
    Schedule serializer for view
        - id
        - day
        - start_hour
        - end_hour
        - request_type
        - teacher (object)
    """

    teacher = TeacherSerializerShort(read_only=True)

    class Meta:
        model = Schedule
        fields = ("id", "day", "start_hour", "end_hour", "request_type", "teacher")


class ScheduleCreationSerializer(serializers.ModelSerializer):
    """
    Schedule serializer for creation
        - day
        - start_hour
        - end_hour
        - request_type
        - teacher (id)
    """

    class Meta:
        model = Schedule
        fields = ("day", "start_hour", "end_hour", "request_type", "teacher")
