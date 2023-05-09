from django.contrib.auth import login

from rest_framework import request
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from knox.views import LoginView as KnoxLoginView

from apps.shared.api import permissions
from apps.authentication.api.serializers import LoginSerializer
from apps.users.api.serializers import UserSerializer


class LoginView(KnoxLoginView, GenericAPIView):
    """Login view that uses knox to generate a token for the user."""

    serializer_class = LoginSerializer
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
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)

        return super(LoginView, self).post(request, format=None)
