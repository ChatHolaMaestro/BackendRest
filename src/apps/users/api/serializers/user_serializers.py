from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserViewSerializer(serializers.ModelSerializer):
    """
    User serializer for viewing.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "phone_number",
            "is_superuser",
            "is_active",
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    """
    User serializer for creation.
    """

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "identification_type",
            "identification_number",
            "phone_number",
        ]

    def create(self, validated_data: dict) -> User:
        """Creates a new user with the given data.

        Args:
            validated_data (dict): Data to create the user.

        Returns:
            User: User object.
        """

        email = validated_data.pop("email")
        password = validated_data.pop("password")

        user = User.objects.create_user_with_password(
            email=email,
            password=password,
            **validated_data,
        )
        return user
