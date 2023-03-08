from django.contrib.auth import get_user_model

from rest_framework import serializers

from apps.users.models.user import User

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
            "is_admin",
            "is_superuser",
            "is_active",
        ]


class UserCreationSerializer(serializers.ModelSerializer):
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
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        """Creates a new user with the given data.

        Args:
            validated_data (dict): serialized data after validation.

        Returns:
            User: User object.
        """
        email = validated_data["email"]
        password = validated_data["password"]
        validated_data.pop("email")
        validated_data.pop("password")
        user = User.objects.create_user(
            email=email, password=password, **validated_data
        )
        return user
