from apps.shared.api.views import GenericModelViewSet
from apps.shared.api.permissions import (
    OrPermission,
    IsAuthenticated,
    IsSuperUser,
    IsAdminRole,
    IsSameUser,
    IsNotSameUser,
)
from apps.users.api.serializers import UserSerializer, UserCreateSerializer


class UserViewSet(GenericModelViewSet):
    serializer_class = UserSerializer
    create_serializer_class = UserCreateSerializer
    update_serializer_class = UserCreateSerializer

    permission_classes = [IsAuthenticated]
    list_permission_classes = [IsAdminRole]
    retrieve_permission_classes = [OrPermission(IsAdminRole, IsSameUser)]
    create_permission_classes = [IsSuperUser]
    update_permission_classes = [IsSuperUser]
    destroy_permission_classes = [IsAdminRole, IsNotSameUser]
