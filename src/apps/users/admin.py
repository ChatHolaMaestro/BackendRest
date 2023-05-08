from django.apps import AppConfig
from django.contrib import admin

from apps.users.models import User

admin.site.register(User)


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.users"
