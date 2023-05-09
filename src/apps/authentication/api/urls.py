from django.urls import path, include
from knox import views as knox_views

from .views import LoginView, RegisterView

urlpatterns = [
    path(r"login/", LoginView.as_view(), name="login"),
    path(r"logout/", knox_views.LogoutView.as_view(), name="logout"),
    path(r"logoutall/", knox_views.LogoutAllView.as_view(), name="logoutall"),
    path(r"register/", RegisterView.as_view(), name="register"),
    path(
        r"password_reset/",
        include("django_rest_passwordreset.urls", namespace="password_reset"),
    ),
]
