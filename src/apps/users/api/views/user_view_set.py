from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet

from apps.users.api.serializers import UserViewSerializer, UserCreateSerializer


class UserViewSet(GenericModelViewSet):
    serializer_class = UserViewSerializer
    serializerCreation = UserCreateSerializer
    serializerUpdate = UserCreateSerializer
