from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.homeworks.homework_api.homework_views.homeworkViewSet import HomeworkViewSet

router = DefaultRouter()

router.register(r'homeworks', HomeworkViewSet, basename='homeworks')

urlpatterns = [
]

urlpatterns += router.urls