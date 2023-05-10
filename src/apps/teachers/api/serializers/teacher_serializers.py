from django.contrib.auth import get_user_model

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.teachers.models import Teacher, ScheduleSlot
from apps.subjects.models import Subject

User = get_user_model()


class TeacherSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Teacher` model. Provides the following fields:
    - id (read-only)
    - user (read-only, nested object)
    - user_id (write-only)
    - subjects (read-only, nested list of objects)
    - schedule_slots (nested list of objects)
    """

    user = serializers.UserNestedSerializer(read_only=True, allow_null=True)
    user_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        source="user",
    )

    subjects = serializers.SubjectNestedSerializer(read_only=True, many=True)
    subjects_id = rf_serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        many=True,
        source="subjects",
    )

    schedule_slots = serializers.ScheduleSlotNestedSerializer(required=False, many=True)

    class Meta:
        model = Teacher
        fields = ("id", "user", "user_id", "subjects", "subjects_id", "schedule_slots")
        extra_kwargs = {"id": {"read_only": True}}

    def create(self, validated_data: dict) -> Teacher:
        """Creates a new `Teacher` instance.

        Args:
            validated_data (dict): data to create the teacher

        Returns:
            Teacher: created teacher
        """

        subjects = validated_data.pop("subjects", [])
        schedule_slots = validated_data.pop("schedule_slots", [])

        teacher, _ = Teacher.objects.get_or_create(**validated_data)

        if subjects != []:
            teacher.subjects.set(subjects)
        if schedule_slots != []:
            ScheduleSlot.objects.filter(teacher=teacher).delete()
            for schedule_slot in schedule_slots:
                schedule_slot["teacher"] = teacher
            ScheduleSlot.objects.bulk_create(
                [ScheduleSlot(**schedule_slot) for schedule_slot in schedule_slots]
            )

        return teacher

    def update(self, instance: Teacher, validated_data: dict) -> Teacher:
        """Updates a `Teacher` with the given data.

        Args:
            instance (Teacher): teacher to update
            validated_data (dict): data to update the teacher

        Returns:
            Teacher: updated teacher
        """

        subjects = validated_data.pop("subjects", [])
        schedule_slots = validated_data.pop("schedule_slots", [])

        teacher = super().update(instance, validated_data)

        if subjects != []:
            teacher.subjects.set(subjects)
        if schedule_slots != []:
            ScheduleSlot.objects.filter(teacher=teacher).delete()
            for schedule_slot in schedule_slots:
                schedule_slot["teacher"] = teacher
            ScheduleSlot.objects.bulk_create(
                [ScheduleSlot(**schedule_slot) for schedule_slot in schedule_slots]
            )

        return teacher
