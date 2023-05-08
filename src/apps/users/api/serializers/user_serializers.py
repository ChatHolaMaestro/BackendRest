from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for the `User` model. Provides the following fields:
    - id (read-only)
    - email
    - password (write-only)
    - first_name
    - last_name
    - identification_type
    - identification_number
    - phone_number
    - role
    - is_superuser
    - is_staff
    - is_active
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
            "role",
            "is_superuser",
            "is_staff",
            "is_active",
        ]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

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
