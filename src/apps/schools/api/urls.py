from rest_framework.routers import DefaultRouter

from apps.schools.api.views import (
    SchoolViewSet,
    SchoolManagerViewSet,
)

router = DefaultRouter()

router.register(r"schools", SchoolViewSet, basename="schools")
router.register(r"school_managers", SchoolManagerViewSet, basename="school_managers")

urlpatterns = []

urlpatterns += router.urls
