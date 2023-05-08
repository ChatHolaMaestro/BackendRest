from django.urls import path, include
from knox import views as knox_views

from .views import LoginView

urlpatterns = [
    path(r"login", LoginView.as_view(), name="login"),
    path(r"logout", knox_views.LogoutView.as_view(), name="logout"),
]
