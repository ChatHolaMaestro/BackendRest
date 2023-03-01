from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.subjects.subject_api.subject_views.subjectViewSet import SubjectViewset

router = DefaultRouter()

router.register(r'subjects', SubjectViewset, basename='subjects')

urlpatterns = [
]

urlpatterns += router.urls