from apps.shared.api.views import GenericModelViewSet
from apps.users.api.serializers import UserViewSerializer, UserCreateSerializer


class UserViewSet(GenericModelViewSet):
    serializer_class = UserViewSerializer
    create_serializer_class = UserCreateSerializer
    update_serializer_class = UserCreateSerializer
