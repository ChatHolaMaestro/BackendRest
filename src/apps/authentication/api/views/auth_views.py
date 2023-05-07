from django.contrib import auth

from rest_framework import generics, permissions
from rest_framework.request import Request
from rest_framework.response import Response

from knox.models import AuthToken

from apps.authentication.api.serializers import LoginSerializer
from apps.users.api.serializers import UserViewSerializer


class LoginView(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request: Request, *args, **kwargs) -> Response:
        """Login an user.

        Args:
            request: request data.
        Returns:
            Response: response with the user and the token.
        Raises:
            Exception: if the serializer is not valid.
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        auth.login(request, user)

        return Response(
            {
                "user": UserViewSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
