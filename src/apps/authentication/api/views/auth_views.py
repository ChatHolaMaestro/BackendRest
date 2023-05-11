from django.contrib.auth import login

from rest_framework import request, status
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView

from django_rest_passwordreset.views import reset_password_request_token

from knox.views import LoginView as KnoxLoginView

from apps.shared.api import permissions
from apps.shared.api.serializers import UserNestedSerializer
from apps.authentication.api.serializers import LoginSerializer, RegisterUserSerializer


class LoginView(KnoxLoginView, GenericAPIView):
    """Login view that uses knox to generate a token for the user."""

    serializer_class = LoginSerializer
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get_user_serializer_class(self) -> UserNestedSerializer:
        """Overwrites super method to return the user serializer.

        Returns:
            UserNestedSerializer: user serializer class.
        """
        return UserNestedSerializer

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

        return super().post(request, format=None)


class RegisterView(GenericAPIView):
    """Register view to create a new user."""

    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.IsAdminRole]

    def post(self, request: request.Request) -> Response:
        """Creates a new user.

        Args:
            request: request data.

        Returns:
            Response: created user.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()

        reset_password_request = request._request
        reset_password_request.POST = {"email": instance.email}
        reset_password_request_token(reset_password_request)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
