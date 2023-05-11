from rest_framework.routers import DefaultRouter

from apps.subjects.api.views import SubjectViewset

router = DefaultRouter()

router.register(r"subjects", SubjectViewset, basename="subjects")

urlpatterns = []

urlpatterns += router.urls
