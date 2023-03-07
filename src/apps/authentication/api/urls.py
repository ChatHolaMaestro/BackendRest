from django.urls import path, include
from .views import LoginView
from knox import views as knox_views

urlpatterns = [
    path("", include("knox.urls")),
    path("login", LoginView.as_view()),
    path("logout", knox_views.LogoutView.as_view(), name="knox-logout"),
]
