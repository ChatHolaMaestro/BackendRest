from django.contrib import auth

from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.models import AuthToken

from apps.authentication.api.serializers import LoginSerializer
from apps.users.user_api.user_serializers import UserViewSerializer


class LoginView(generics.GenericAPIView):

    serializer_class = LoginSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs) -> Response:
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
        print("user", user)
        auth.login(request, user)

        serialized_user = UserViewSerializer(
            user, context=self.get_serializer_context()
        )
        print("serialized_user", serialized_user)
        return Response(
            {
                "user": UserViewSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )
