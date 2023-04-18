from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.students.api.views import (
    StudentViewSet,
    RelativeViewSet,
)

router = DefaultRouter()

router.register(r"students", StudentViewSet, basename="students")
router.register(r"relatives", RelativeViewSet, basename="relatives")

urlpatterns = []

urlpatterns += router.urls
