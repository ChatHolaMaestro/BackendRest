from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.schools.school_api.school_views.schoolViewSet import SchoolViewset, SchoolManagerViewset

router = DefaultRouter()

router.register(r'schools', SchoolViewset, basename='schools')
router.register(r'school_managers', SchoolManagerViewset, basename='school_managers')

urlpatterns = [
]

urlpatterns += router.urls