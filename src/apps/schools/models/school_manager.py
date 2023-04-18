from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.users.models.user import User

from .school import School


class SchoolManager(SharedModelHistorical):
    """
    Model which represents a school manager
    """

    # Could be null if the user has not been created yet
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
