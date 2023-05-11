from collections import OrderedDict
from rest_framework import serializers


class NonNullToRepresentationMixin:
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


class NonNullSerializer(serializers.Serializer, NonNullToRepresentationMixin):
    """Serializer that removes null values from the response."""


class NonNullModelSerializer(serializers.ModelSerializer, NonNullToRepresentationMixin):
    """ModelSerializer that removes null values from the response."""
