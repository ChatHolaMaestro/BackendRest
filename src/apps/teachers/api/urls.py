from rest_framework.routers import DefaultRouter

from apps.teachers.api.views import TeacherViewSet, ScheduleViewSet

router = DefaultRouter()

router.register(r"teachers", TeacherViewSet, basename="teachers")
router.register(r"schedules", ScheduleViewSet, basename="schedules")

urlpatterns = []

urlpatterns += router.urls
