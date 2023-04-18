from rest_framework import serializers

from apps.subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    Subject serializer
        - id
        - name
    """

    class Meta:
        model = Subject
        fields = ("id", "name")
