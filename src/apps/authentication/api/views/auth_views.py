from django.contrib.auth import login

from rest_framework import permissions, request
from rest_framework.response import Response

from rest_framework.generics import GenericAPIView

from knox.views import LoginView as KnoxLoginView

from apps.authentication.api.serializers import LoginSerializer
from apps.users.api.serializers import UserSerializer


class LoginView(KnoxLoginView):
    """Login view that uses knox to generate a token for the user."""

    permission_classes = [permissions.AllowAny]

    def get_user_serializer_class(self) -> UserSerializer:
        """Overwrites super method to return the user serializer.

        Returns:
            UserSerializer: user serializer class.
        """
        return UserSerializer

    def post(self, request: request.Request) -> Response:
        """Authenticates the user and returns the user, token and expiry date
        if the credentials are correct.

        Args:
            request: request data.

        Returns:
            Response: user, token and expiry date.
        """
        serializer = LoginSerializer(data=request.data, context=self.get_context())
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)

        return super(LoginView, self).post(request, format=None)
