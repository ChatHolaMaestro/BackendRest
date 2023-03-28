from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    OrPermission,
    IsAuthenticated,
    IsAdminRole,
    IsSameUser,
    IsNotSameUser,
)
from apps.users.api.serializers import UserViewSerializer, UserCreateSerializer


class UserViewSet(GenericModelViewSet):
    serializer_class = UserViewSerializer
    create_serializer_class = UserCreateSerializer
    update_serializer_class = UserCreateSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [IsAdminRole]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsSameUser)]
    create_permission_classes = [IsAdminRole]
    update_permission_classes = [IsAdminRole]
    destroy_permission_classes = [IsAdminRole, IsNotSameUser]
