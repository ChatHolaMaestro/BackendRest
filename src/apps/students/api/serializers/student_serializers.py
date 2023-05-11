from apps.shared.api import serializers
from apps.students.models import Student


class StudentViewSerializer(serializers.NonNullModelSerializer):
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

    relatives = serializers.RelativeSerializerShort(many=True, read_only=True)
    school = serializers.SchoolSerializerShort(read_only=True)

    class Meta:
        model = Student
        exclude = ["is_active", "created_date", "modified_date", "deleted_date"]


class StudentCreationSerializer(serializers.NonNullModelSerializer):
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
