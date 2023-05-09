from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.subjects.models import Subject
from apps.teachers.models import Teacher, ScheduleSlot
from apps.schools.models import School, SchoolManager

User = get_user_model()


class UserNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `User` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - email
    - first_name
    - last_name
    - identification_type
    - identification_number
    - phone_number
    - role
    """

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "phone_number",
            "role",
        )


class ScheduleSlotNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `ScheduleSlot` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - day_of_week
    - start_time
    - end_time
    - request_type
    """

    class Meta:
        model = ScheduleSlot
        fields = ("id", "day_of_week", "start_time", "end_time", "request_type")
        extra_kwargs = {"id": {"read_only": True}}


class SubjectNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `Subject` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - name
    """

    class Meta:
        model = Subject
        fields = ("id", "name")


class TeacherNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `Teacher` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - subjects (list of `SubjectNestedSerializer`)
    - schedule_slots (list of `ScheduleSlotNestedSerializer`)
    """

    subjects = SubjectNestedSerializer(many=True)
    schedule_slots = ScheduleSlotNestedSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ("id", "subjects", "schedule_slots")


class SchoolNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `School` model. To be used as a nested serializer.
    Provides the following fields:
    - id
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


class SchoolManagerNestedSerializer(serializers.ModelSerializer):
    """Serializer for the `SchoolManager` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - school (`SchoolNestedSerializer`)
    """

    school = SchoolNestedSerializer()

    class Meta:
        model = SchoolManager
        fields = ("id", "school")
