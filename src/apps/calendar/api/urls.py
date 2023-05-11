from django.urls import path

from .views import NewEventView

urlpatterns = [
    path(r"events/", NewEventView.as_view(), name="new-event"),
]
