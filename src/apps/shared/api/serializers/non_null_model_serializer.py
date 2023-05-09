from collections import OrderedDict
from rest_framework import serializers


class NonNullModelSerializer(serializers.ModelSerializer):
    """Serializer that removes null values from the response."""

    def to_representation(self, instance) -> OrderedDict:
        """Updated serializer method to remove null values from the response.

        Args:
            instance: model instance to serialize.

        Returns:
            OrderedDict: serialized model instance.
        """
        result = super().to_representation(instance)
        return OrderedDict(
            [(key, result[key]) for key in result if result[key] is not None]
        )
