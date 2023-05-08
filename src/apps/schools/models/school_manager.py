from django.db import models
from django.contrib.auth import get_user_model

from apps.shared.models import SharedModelHistorical

from .school import School

User = get_user_model()


class SchoolManager(SharedModelHistorical):
    """
    Model that represents a school manager. A school manager is a user that
    manages a school.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
