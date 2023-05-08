from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.subjects.models import Subject
from apps.users.models.user import User


class Teacher(SharedModelHistorical):
    """
    Model which represents a teacher
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        if self.user:
            return f"Profesor {self.user}"
        return f"Profesor {self.id}"
