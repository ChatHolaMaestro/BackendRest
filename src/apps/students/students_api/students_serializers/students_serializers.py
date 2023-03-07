from rest_framework import serializers

from apps.students.students_models import Student
from apps.shared.shared_api.shared_serializers.ShortSerializers import (
    RelativeSerializerShort,
    SchoolSerializerShort,
)


class StudentViewSerializer(serializers.ModelSerializer):
    """
    Student Serializer for view:
        - id
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - grade
        - sex
        - age
        - working_hours
        - relatives (object)
        - school (object)
    """

    relatives = RelativeSerializerShort(many=True, read_only=True)
    school = SchoolSerializerShort(read_only=True)

    class Meta:
        model = Student
        exclude = ["is_active", "created_date", "modified_date", "deleted_date"]


class StudentCreationSerializer(serializers.ModelSerializer):
    """
    Student Serializer for creation:
        - name
        - last_name
        - identification_type
        - identification_number
        - phone_number
        - grade
        - sex
        - age
        - working_hours
        - relatives (ids)
        - school (id)
    """

    class Meta:
        model = Student
        exclude = ["is_active", "created_date", "modified_date", "deleted_date"]
