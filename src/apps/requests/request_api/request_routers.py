from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.requests.request_api.request_views.requestViewSet import RequestViewSet

router = DefaultRouter()

router.register(r'requests', RequestViewSet, basename='requests')

urlpatterns = [
]

urlpatterns += router.urls