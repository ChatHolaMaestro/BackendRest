from django.db import models
from django.contrib.auth import get_user_model

from apps.shared.models import SharedModelHistorical
from apps.subjects.models import Subject

User = get_user_model()


class Teacher(SharedModelHistorical):
    """
    Model that represents a teacher. A teacher is a user that has subjects
    and a schedule.
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True, related_name="teacher"
    )
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        if self.user:
            return self.user
        return self.id
