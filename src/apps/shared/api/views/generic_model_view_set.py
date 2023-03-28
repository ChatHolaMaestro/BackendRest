from django.conf import settings

from rest_framework import status, request, serializers, viewsets
from rest_framework.response import Response

from apps.shared.api.permissions import BasePermission, OrPermission


class GenericModelViewSet(viewsets.ModelViewSet):
    serializer_class = None
    create_serializer_class = None
    update_serializer_class = None

    list_permission_classes = []
    retrieve_permission_classes = []
    create_permission_classes = []
    update_permission_classes = []
    destroy_permission_classes = []

    def get_queryset(self):
        model = self.get_serializer().Meta.model
        return model.objects.filter(is_active=True)

    def get_serializer_class(self) -> serializers.Serializer:
        if self.action == "create":
            if self.create_serializer_class:
                return self.create_serializer_class
        elif self.action == "update":
            if self.update_serializer_class:
                return self.update_serializer_class

        return super().get_serializer_class()

    def _get_action_permissions(
        self, action_permission_classes: list[BasePermission]
    ) -> list[BasePermission]:
        return [
            permission() if not isinstance(permission, OrPermission) else permission
            for permission in (action_permission_classes + self.permission_classes)
        ]

    def get_permissions(self) -> list[BasePermission]:
        if settings.PERMISSIONS_DISABLED:
            return []

        if self.action == "list":
            return self._get_action_permissions(self.list_permission_classes)
        elif self.action == "retrieve":
            return self._get_action_permissions(self.retrieve_permission_classes)
        elif self.action == "create":
            return self._get_action_permissions(self.create_permission_classes)
        elif self.action == "update":
            return self._get_action_permissions(self.update_permission_classes)
        elif self.action == "destroy":
            return self._get_action_permissions(self.destroy_permission_classes)
        # if its a custom @action, the action may pass a name kwarg
        # and the view may implement an action_name_permission_classes attribute
        elif hasattr(self, f"{self.action}_permission_classes"):
            return self._get_action_permissions(
                getattr(self, f"{self.action}_permission_classes")
            )

        return super().get_permissions()

    def list(self, request: request.Request, *args, **kwargs) -> Response:
        """Get all objects of the model.

        Args:
            request (request.Request): HTTP request information

        Returns:
            Response: HTTP response with the objects
        """

        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: request.Request, *args, **kwargs) -> Response:
        """Get an object of the model by id.

        Args:
            request (request.Request): HTTP request information with the id of the object

        Returns:
            Response: HTTP response with the object or 404 if the object is not found
        """

        instance = self.get_object()
        if instance:
            return Response(
                self.get_serializer(instance).data, status=status.HTTP_200_OK
            )
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    def create(self, request: request.Request, *args, **kwargs) -> Response:
        """Create an object of the model.

        Args:
            request (request.Request): HTTP request information

        Returns:
            Response: HTTP response with the created object

        Raises:
            Exception: If the object is not created
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request: request.Request, *args, **kwargs) -> Response:
        """Update an object of the model.

        Args:
            request (request.Request): HTTP request information with the id of the object

        Returns:
            Response: HTTP response with the updated object or 404 if the object is not found

        Raises:
            Exception: If the object is not updated
        """

        instance = self.get_object()
        if instance:
            serializer = self.get_serializer(instance, data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request: request.Request, *args, **kwargs) -> Response:
        """
        Delete an object of the model (logical delete).

        Args:
            request (request.Request): HTTP request information with the id of the object

        Returns:
            Response: HTTP response 200 if the object is deleted or 404 if the object is not found
        """

        instance = self.get_object()
        if instance:
            instance.is_active = False
            instance.save()
            return Response(
                {"message": "Object deleted successfully"}, status=status.HTTP_200_OK
            )
        return Response({"error": "Object not found"}, status=status.HTTP_404_NOT_FOUND)
