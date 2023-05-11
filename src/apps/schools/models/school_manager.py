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

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="school_manager",
    )
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="school_managers"
    )

    def __str__(self):
        return "{{id: {}, user: {}, school: {}}}".format(
            self.id, self.user, self.school
        )
