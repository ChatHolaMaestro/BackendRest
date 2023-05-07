from django.urls import path, include
from knox import views as knox_views

from .views import LoginView

urlpatterns = [
    path(r"login", LoginView.as_view()),
    path(r"logout", knox_views.LogoutView.as_view(), name="knox_logout"),
]
