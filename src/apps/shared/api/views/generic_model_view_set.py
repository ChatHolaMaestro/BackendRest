from typing import Iterable

from django.conf import settings
from django.db.models import Model

from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from apps.shared.api.permissions import BasePermission, OrPermission


class GenericModelViewSet(ModelViewSet):
    http_method_names = [
        "get",
        "post",
        "put",
        "delete",
        "head",
        "options",
        "trace",
    ]

    serializer_class = None
    create_serializer_class = None
    update_serializer_class = None

    list_permission_classes = []
    retrieve_permission_classes = []
    create_permission_classes = []
    update_permission_classes = []
    destroy_permission_classes = []

    def _get_default_serializer_class(self) -> ModelSerializer:
        """Returns the default serializer class of the view, which is the
        `serializer_class` attribute. The view must implement this attribute,
        since it will raise an assertion error if it's not.

        Returns:
            ModelSerializer: `serializer_class` attribute
        """
        assert (
            self.serializer_class is not None
        ), "{} must define a `serializer_class` attribute".format(
            self.__class__.__name__
        )
        return self.serializer_class

    def get_serializer_class(self) -> ModelSerializer:
        """Returns the serializer class to use for the current action. "create"
        and "update" may have their own serializer classes. Otherwise, the default
        serializer class is used (`serializer_class`).

        Returns:
            ModelSerializer: the serializer class to use
        """
        if self.action == "create":
            if self.create_serializer_class:
                return self.create_serializer_class
        elif self.action == "update":
            if self.update_serializer_class:
                return self.update_serializer_class
        return self._get_default_serializer_class()

    def get_default_serializer(self, *args, **kwargs) -> ModelSerializer:
        """Returns the default serializer instance that should be used for
        validating and deserializing input, and for serializing output.

        Returns:
            ModelSerializer: `serializer_class` instantiated
        """
        serializer_class = self._get_default_serializer_class()
        kwargs.setdefault("context", self.get_serializer_context())
        return serializer_class(*args, **kwargs)

    def _get_action_permissions(
        self, action_permission_classes: Iterable[BasePermission]
    ) -> list[BasePermission]:
        """Each action has its own permission classes, plus the default permission
        classes of the view. They should be merged and instantiated. Additionally,
        a permission class can be an OrPermission, which shouldn't be instantiated
        (because it already is when it's defined in the view).

        Args:
            action_permission_classes (Iterable[BasePermission]): the action-specific
            permission classes

        Returns:
            list[BasePermission]: the instantiated permission classes
        """
        return [
            permission() if not isinstance(permission, OrPermission) else permission
            for permission in (action_permission_classes + self.permission_classes)
        ]

    def get_permissions(self) -> list[BasePermission]:
        """This method is called by the framework when a request is initiated to
        the view. It returns the permission classes that will be used to check
        if the request is authorized to access the view. Each action has its own
        permission classes, plus the default permission classes of the view
        (`permission_classes`).

        Any custom `@action` may also define its own permission classes. The action
        must be created with a `name` kwarg, and the view must implement an attribute
        with the name `name_permission_classes` (where `name` is the name of the action).
        For example, if the action is `@action(detail=True, name="my_action")`, the view
        may implement an attribute called `my_action_permission_classes`.

        Returns:
            list[BasePermission]: the instantiated permission classes
        """
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
        # custom @action
        elif hasattr(self, f"{self.action}_permission_classes"):
            return self._get_action_permissions(
                getattr(self, f"{self.action}_permission_classes")
            )

        return super().get_permissions()

    def list(self, request: Request, *args, **kwargs) -> Response:
        """Returns a list of all objects of the model associated with the view.
        This is an action associated with the GET method called at the root of
        the view's endpoint.

        Args:
            request (Request): request information

        Returns:
            Response: list of objects of the model
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, *args, **kwargs) -> Response:
        """Returns an object of the model associated with the view. This is an
        action associated with the GET method called at the endpoint of the view
        with the id as a path variable. If the object is not found, a 404 response
        is returned.

        Args:
            request (Request): request information

        Returns:
            Response: retrieved object of the model or 404 if not found
        """
        instance = self.get_object()  # will raise 404 if not found
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request: Request, *args, **kwargs) -> Response:
        """Creates an object of the model associated with the view. This is an
        action associated with the POST method called at the root of the view's
        endpoint. If the object is not created, a 400 response is returned.

        Args:
            request (Request): request information

        Returns:
            Response: created object of the model

        Raises:
            Exception: if the object is not created
        """
        serializer = self.get_serializer(data=request.data)
        if(not serializer.is_valid()):
            print(serializer.errors)
        
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        # returning the created object should use the default serializer_class
        # since the create_serializer_class may have write-only fields
        object = self.get_queryset().get(pk=serializer.instance.pk)
        serializer = self.get_default_serializer(object)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

    def update(self, request: Request, *args, **kwargs) -> Response:
        """Updates an object of the model associated with the view. This is an
        action associated with the PUT method called at the endpoint of the view
        with the id as a path variable. If the object is not found, a 404 response
        is returned.

        Args:
            request (Request): request information

        Returns:
            Response: updated object of the model

        Raises:
            Exception: if the object is not updated
        """
        instance = self.get_object()  # will raise 404 if not found

        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, "_prefetched_objects_cache", None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        # returning the updated object should use the default serializer_class
        object = self.get_queryset().get(pk=serializer.instance.pk)
        serializer = self.get_default_serializer(object)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request: Request, *args, **kwargs) -> Response:
        """Deletes an object of the model associated with the view. This is an
        action associated with the DELETE method called at the endpoint of the view
        with the id as a path variable. If the object is not found, a 404 response
        is returned.

        Args:
            request (Request): request information

        Returns:
            Response: 200 if the object is deleted, 404 if not found
        """
        instance = self.get_object()  # will raise 404 if not found
        self.perform_destroy(instance)

        return Response(
            {"message": "Object deleted successfully"}, status=status.HTTP_200_OK
        )

    def perform_destroy(self, instance: Model):
        """Deletes an object according to the `destroy` action. The deletion is
        done by setting the `is_active` attribute to False.

        Args:
            instance (Model): object to delete
        """
        # prefer either logical or real deletion

        # instance.is_active = False
        # instance.save()
        super().perform_destroy(instance)
