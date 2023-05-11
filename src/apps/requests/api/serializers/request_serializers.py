from apps.shared.api import serializers
from apps.requests.models import Request


class RequestViewSerializer(serializers.NonNullModelSerializer):
    """
    Request Serializer for View
        - id
        - status
        - request_type
        - created_date
        - contact_times
        - student (object)
        - teacher (object)
        - subject (object)
    """

    student = serializers.StudentSerializerShort()
    teacher = serializers.TeacherSerializerShort()
    subject = serializers.SubjectNestedSerializer()
    homework = serializers.HomeworkSerializerShort()  # could be null

    class Meta:
        model = Request
        fields = [
            "id",
            "status",
            "request_type",
            "created_date",
            "contact_times",
            "student",
            "teacher",
            "subject",
            "homework",
        ]


class RequestCreationSerializer(serializers.NonNullModelSerializer):
    """
    Request Serializer for Creation
        - status
        - request_type
        - contact_times
        - student (id)
        - teacher (id)
        - subject (id)
    """

    class Meta:
        model = Request
        fields = [
            "status",
            "request_type",
            "contact_times",
            "student",
            "teacher",
            "subject",
        ]
