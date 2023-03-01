from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.teachers.teacher_api.teacher_views.teacherViewSet import TeacherViewSet, ScheduleViewSet

router = DefaultRouter()

router.register(r'teachers', TeacherViewSet, basename='teachers')
router.register(r'schedules', ScheduleViewSet, basename='schedules')

urlpatterns = [
]

urlpatterns += router.urls