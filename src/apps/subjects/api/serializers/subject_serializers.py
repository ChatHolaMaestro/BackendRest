from apps.shared.api import serializers
from apps.subjects.models import Subject


class SubjectSerializer(serializers.NonNullModelSerializer):
    """Serializer for the `Subject` model. Provides the following fields:
    - id (read-only)
    - name
    """

    class Meta:
        model = Subject
        fields = ("id", "name")
        extra_kwargs = {"id": {"read_only": True}}
