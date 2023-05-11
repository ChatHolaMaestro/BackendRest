from rest_framework.routers import DefaultRouter

from apps.requests.api.views import RequestViewSet

router = DefaultRouter()

router.register(r"requests", RequestViewSet, basename="requests")

urlpatterns = []

urlpatterns += router.urls
