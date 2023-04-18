from rest_framework.routers import DefaultRouter

from apps.homeworks.api.views import HomeworkViewSet

router = DefaultRouter()

router.register(r"homeworks", HomeworkViewSet, basename="homeworks")

urlpatterns = []

urlpatterns += router.urls
