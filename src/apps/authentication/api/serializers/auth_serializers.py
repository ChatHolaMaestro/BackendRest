from django.contrib.auth import authenticate, get_user_model

from rest_framework import serializers

User = get_user_model()


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data: dict) -> User:
        """Validates the data and returns the user if the credentials are correct.

        Args:
            data (dict): validated data.

        Raises:
            serializers.ValidationError: if the credentials are incorrect.

        Returns:
            User: User object.
        """

        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect credentials")
