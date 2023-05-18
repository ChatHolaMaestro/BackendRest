from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.teachers.models import Teacher, ScheduleSlot
from apps.schools.models import School, SchoolManager
from apps.subjects.models import Subject

User = get_user_model()


class UserSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `User` model. Provides the following fields:
    - id (read-only)
    - email
    - password (write-only)
    - first_name
    - last_name
    - identification_type
    - identification_number
    - phone_number
    - role
    - is_superuser
    - is_staff
    - is_active
    - school_manager (read-only, nested object)
    - school (write-only)
    - teacher (read-only, nested object)
    - subjects (write-only)
    - schedules (nested list of objects)
    """

    school_manager = serializers.SchoolManagerNestedSerializer(
        read_only=True, allow_null=True
    )
    school = rf_serializers.PrimaryKeyRelatedField(
        queryset=School.objects.all(),
        write_only=True,
        required=False,
    )

    teacher = serializers.TeacherNestedSerializer(read_only=True, allow_null=True)
    subjects = rf_serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(),
        write_only=True,
        required=False,
        many=True,
    )
    schedules = serializers.ScheduleSlotNestedSerializer(
        write_only=True, required=False, many=True
    )

    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "phone_number",
            "role",
            "is_superuser",
            "is_staff",
            "is_active",
            "school_manager",
            "school",
            "teacher",
            "subjects",
            "schedules",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "password": {"write_only": True, "required": False},
        }

    def create(self, validated_data: dict) -> User:
        """Creates a new user with the given data.

        Args:
            validated_data (dict): data to create the user.

        Returns:
            User: User object.
        """

        email = validated_data.pop("email", None)
        password = validated_data.pop("password", None)

        school = validated_data.pop("school", None)
        subjects = validated_data.pop("subjects", [])
        schedule_slots = validated_data.pop("schedules", [])

        user = User.objects.create_user_with_password(
            email=email,
            password=password,
            **validated_data,
        )

        '''
        if validated_data["role"] == User.SCHOOL_MANAGER:
            if school is None:
                user.delete()
                raise rf_serializers.ValidationError(
                    {
                        "school": [
                            _("This field is required when role is school manager")
                        ]
                    }
                )
            SchoolManager.objects.create(user=user, school=school)
        elif validated_data["role"] == User.TEACHER:
            teacher = Teacher.objects.create(user=user)
            teacher.subjects.set(subjects)

            for schedule_slot_data in schedule_slots:
                schedule_slot_data["teacher"] = teacher
            ScheduleSlot.objects.bulk_create(
                [ScheduleSlot(**data) for data in schedule_slots]
            )
        '''

        return user

    def update(self, instance: User, validated_data: dict) -> User:
        """Updates a user with the given data.

        Args:
            instance (User): user to update.
            validated_data (dict): data to update the user.

        Returns:
            User: updated user object.
        """

        password = validated_data.pop("password", None)

        school = validated_data.pop("school", None)
        subjects = validated_data.pop("subjects", [])
        schedule_slots = validated_data.pop("schedules", [])

        user = super().update(instance, validated_data)

        if password is not None:
            user.set_password(password)
            user.save()

        if instance.role == User.SCHOOL_MANAGER and school is not None:
            SchoolManager.objects.update_or_create(
                user=user, defaults={"school": school}
            )
        if instance.role == User.TEACHER:
            teacher, __ = Teacher.objects.get_or_create(user=user)
            if subjects != []:
                teacher.subjects.set(subjects)
            if schedule_slots != []:
                ScheduleSlot.objects.filter(teacher=teacher).delete()
                for schedule_slot in schedule_slots:
                    schedule_slot["teacher"] = teacher
                ScheduleSlot.objects.bulk_create(
                    [ScheduleSlot(**data) for data in schedule_slots]
                )

        return user
