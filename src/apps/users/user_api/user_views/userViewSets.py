from django.shortcuts import render

# import generic view set
from apps.shared.shared_api.shared_views.GenericModelViewSets import GenericModelViewSet
from apps.users.user_api.user_serializers.userSerializers import UserViewSerializer, UserCreationSerializer

class UserViewSet(GenericModelViewSet):
    """
    Generic viewset for user model
        - GET: list all users
        - POST: create a user
        - GET(id): get a user by id
        - PUT(id): update a user by id
        - DELETE(id): delete a user by id
    """
    serializer_class = UserViewSerializer
    serializerCreation = UserCreationSerializer
    serializerUpdate = UserCreationSerializer