from rest_framework import serializers as rf_serializers

from apps.shared.api import serializers
from apps.requests.models import Request
from apps.students.models import Student
from apps.teachers.models import Teacher
from apps.subjects.models import Subject
from apps.homeworks.models import Homework


class RequestSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Request` model intended for list/retrieve actions.
    Provides the following fields:
    - id
    - status
    - request_type
    - created_date
    - contact_times
    - student (nested object)
    - teacher (nested object)
    - subject (nested object)
    - homework (nested object)
    """

    student = serializers.StudentNestedSerializer(read_only=True, allow_null=True)
    teacher = serializers.TeacherOfRequestNestedSerializer(
        read_only=True, allow_null=True
    )
    subject = serializers.SubjectNestedSerializer(read_only=True, allow_null=True)
    homework = serializers.HomeworkNestedSerializer(read_only=True, allow_null=True)

    class Meta:
        model = Request
        fields = (
            "id",
            "status",
            "request_type",
            "created_date",
            "contact_times",
            "student",
            "teacher",
            "subject",
            "homework",
        )
        extra_kwargs = {"id": {"read_only": True}}


class WriteRequestSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Request` model intended for create/update actions.
    Provides the following fields:
    - status
    - request_type
    - created_date
    - contact_times
    - student (id)
    - teacher (id)
    - subject (id)
    - homework (id)
    """

    student = rf_serializers.PrimaryKeyRelatedField(
        queryset=Student.objects.all(), write_only=True, required=False
    )
    teacher = rf_serializers.PrimaryKeyRelatedField(
        queryset=Teacher.objects.all(), write_only=True, required=False
    )
    subject = rf_serializers.PrimaryKeyRelatedField(
        queryset=Subject.objects.all(), write_only=True, required=False
    )
    homework = rf_serializers.PrimaryKeyRelatedField(
        queryset=Homework.objects.all(), write_only=True, required=False
    )

    class Meta:
        model = Request
        fields = (
            "status",
            "request_type",
            "created_date",
            "contact_times",
            "student",
            "teacher",
            "subject",
            "homework",
        )
