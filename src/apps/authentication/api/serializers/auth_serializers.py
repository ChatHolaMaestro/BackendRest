from django.contrib.auth import authenticate, get_user_model
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.teachers.models import Teacher, ScheduleSlot
from apps.schools.models import School, SchoolManager
from apps.subjects.models import Subject

User = get_user_model()


class LoginSerializer(rf_serializers.Serializer):
    email = rf_serializers.EmailField(label=_("Email"), write_only=True)
    password = rf_serializers.CharField(
        label=_("Password"),
        style={"input_type": "password"},
        trim_whitespace=False,
        write_only=True,
    )
    token = rf_serializers.CharField(label="Token", read_only=True)

    def validate(self, attrs: dict) -> dict:
        """Validates the data and inserts the user in the context if the
        credentials are correct.

        Args:
            attrs (dict): data to validate.

        Returns:
            dict: validated data with the user.

        Raises:
            ValidationError: if the credentials are incorrect or not provided.
        """

        email = attrs.get("email")
        password = attrs.get("password")

        if email and password:
            user = authenticate(
                request=self.context.get("request"),
                email=email,
                password=password,
            )

            if not user:
                msg = _("Unable to login with provided credentials.")
                raise rf_serializers.ValidationError(msg, code="authorization")
        else:
            msg = _('Must include "email" and "password".')
            raise rf_serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class RegisterUserSerializer(serializers.NonNullModelSerializer):
    """Serializer for registering a new `User` model. Provides the following fields:
    - id (read-only)
    - email
    - first_name
    - last_name
    - identification_type
    - identification_number
    - phone_number
    - role
    - is_superuser (read-only)
    - is_staff (read-only)
    - is_active (read-only)
    - school_manager (read-only, nested object)
    - school (write-only)
    - teacher (read-only, nested object)
    - subjects (write-only)
    - schedule_slots (nested list of objects)
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
    schedule_slots = serializers.ScheduleSlotNestedSerializer(
        write_only=True, required=False, many=True
    )

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
            "is_superuser",
            "is_staff",
            "is_active",
            "school_manager",
            "school",
            "teacher",
            "subjects",
            "schedule_slots",
        )
        extra_kwargs = {
            "id": {"read_only": True},
            "is_superuser": {"read_only": True},
            "is_staff": {"read_only": True},
            "is_active": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        """Creates a new user with the given data.

        Args:
            validated_data (dict): data to create the user.

        Returns:
            User: User object.
        """

        email = validated_data.pop("email", None)

        school = validated_data.pop("school", None)
        subjects = validated_data.pop("subjects", [])
        schedule_slots = validated_data.pop("schedule_slots", [])

        user = User.objects.create_user_without_password(
            email=email,
            **validated_data,
        )

        if validated_data["role"] == User.SCHOOL_MANAGER:
            if school is None:
                user.delete()
                raise rf_serializers.ValidationError(
                    {"school": ["This field is required when role is school manager"]}
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

        return user
