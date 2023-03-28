from rest_framework import serializers

from apps.teachers.teacher_models.teacherModels import Teacher
from apps.subjects.subject_api.subject_serializers.subjectSerializer import (
    SubjectSerializer,
)
from apps.shared.api.serializers import ScheduleSerializerShort, UserSerializerShort


class TeacherViewSerializer(serializers.ModelSerializer):
    """
    Teacher serializer for view
        - id
        - subjects (objects)
        - schedules (objects)
    """

    user = UserSerializerShort(read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    schedules = ScheduleSerializerShort(many=True, read_only=True)

    class Meta:
        model = Teacher
        fields = ("id", "user", "subjects", "schedules")


class TeacherCreationSerializer(serializers.ModelSerializer):
    """
    Teacher serializer for creation
        - subjects (ids)
        - schedules (ids)
    """

    class Meta:
        model = Teacher
        fields = ("user", "subjects", "schedules")
