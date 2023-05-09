from django.apps import AppConfig
from django.contrib import admin

from apps.users.models import User

admin.site.register(User)
