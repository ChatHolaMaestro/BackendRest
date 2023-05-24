from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.teachers.models import Teacher, ScheduleSlot
from apps.subjects.models import Subject

User = get_user_model()


class TeacherSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Teacher` model intended for list/retrieve actions.
    Provides the following fields:
    - id
    - user (nested object)
    - subjects (nested list of objects)
    - schedules (nested list of objects)
    """

    user = serializers.UserNestedSerializer(read_only=True, allow_null=True)
    subjects = serializers.SubjectNestedSerializer(read_only=True, many=True)
    schedules = serializers.ScheduleSlotNestedSerializer(
        read_only=True, many=True, source="schedule_slots"
    )

    class Meta:
        model = Teacher
        fields = ("id", "user", "subjects", "schedules")
        extra_kwargs = {"id": {"read_only": True}}


class WriteTeacherSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Teacher` model intended for create/write actions.
    Provides the following fields:
    - user (id)
    - subjects (list of ids)
    - schedules (list of ids)
    """

    user = rf_serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), write_only=True, required=False
    )
    subjects = rf_serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        many=True,
    )
    schedules = serializers.ScheduleSlotNestedSerializer(
        write_only=True, required=False, many=True, source="schedule_slots"
    )

    class Meta:
        model = Teacher
        fields = ("user", "subjects", "schedules")

    def validate(self, data):
        user = data.get("user")

        if user:
            if Teacher.objects.filter(user=user).exists():
                raise rf_serializers.ValidationError(_("User is already a teacher."))

        if not self.instance:
            if not user:
                raise rf_serializers.ValidationError(
                    _("User is required when creating a teacher.")
                )

        return data

    def create(self, validated_data: dict) -> Teacher:
        """Creates a new `Teacher` instance.

        Args:
            validated_data (dict): data to create the teacher

        Returns:
            Teacher: created teacher
        """

        user = validated_data.pop("user")

        teacher = Teacher.objects.create(user=user)

        if "subjects" in validated_data:
            teacher.subjects.set(validated_data["subjects"])
            teacher.save()
        if "schedule_slots" in validated_data:
            schedule_slots = validated_data.pop("schedule_slots")
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

        teacher = Teacher.objects.get(pk=instance.pk)

        if "user" in validated_data:
            teacher.user = validated_data["user"]
            teacher.save()
        if "subjects" in validated_data:
            teacher.subjects.set(validated_data["subjects"])
            teacher.save()
        if "schedule_slots" in validated_data:
            schedule_slots = validated_data.pop("schedule_slots")
            ScheduleSlot.objects.filter(teacher=teacher).delete()
            for schedule_slot in schedule_slots:
                schedule_slot["teacher"] = teacher
            ScheduleSlot.objects.bulk_create(
                [ScheduleSlot(**schedule_slot) for schedule_slot in schedule_slots]
            )

        return teacher
