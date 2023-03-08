from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.user_api.user_views.userViewSets import UserViewSet

router = DefaultRouter()

router.register(r"users", UserViewSet, basename="users")

urlpatterns = [
]

urlpatterns += router.urls