from django.contrib.auth import get_user_model

from apps.subjects.models import Subject
from apps.teachers.models import Teacher, ScheduleSlot
from apps.schools.models import School, SchoolManager

from .non_null_serializers import NonNullModelSerializer

User = get_user_model()


class UserNestedSerializer(NonNullModelSerializer):
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
    - is_superuser
    - is_staff
    - is_active
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
            "is_superuser",
            "is_staff",
            "is_active",
        )


class ScheduleSlotNestedSerializer(NonNullModelSerializer):
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


class SubjectNestedSerializer(NonNullModelSerializer):
    """Serializer for the `Subject` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - name
    """

    class Meta:
        model = Subject
        fields = ("id", "name")


class TeacherNestedSerializer(NonNullModelSerializer):
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


class TeacherOfScheduleSlotNestedSerializer(NonNullModelSerializer):
    """Serializer for the `Teacher` model nested inside a `ScheduleSlot` model.
    Provides the following fields:
    - id
    - user (`UserNestedSerializer`)
    - subjects (list of `SubjectNestedSerializer`)
    """

    user = UserNestedSerializer(allow_null=True)
    subjects = SubjectNestedSerializer(many=True)

    class Meta:
        model = Teacher
        fields = ("id", "user", "subjects")


class SchoolNestedSerializer(NonNullModelSerializer):
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


class SchoolManagerNestedSerializer(NonNullModelSerializer):
    """Serializer for the `SchoolManager` model. To be used as a nested serializer.
    Provides the following fields:
    - id
    - school (`SchoolNestedSerializer`)
    """

    school = SchoolNestedSerializer()

    class Meta:
        model = SchoolManager
        fields = ("id", "school")
