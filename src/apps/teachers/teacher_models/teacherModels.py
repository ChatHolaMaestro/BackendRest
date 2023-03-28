from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.shared.models.choices import WeekDays, RequestType
from apps.subjects.subject_models.subjectModels import Subject
from apps.users.models.user import User


class Teacher(SharedModelHistorical):
    """
    Model which represents a teacher
    """

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, null=True
    )  # Could be blank and null
    subjects = models.ManyToManyField(Subject, related_name="teachers")

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        if self.user:
            return f"Profesor {self.user}"
        return f"Profesor {self.id}"


class Schedule(SharedModelHistorical):
    """
    Model which represents a schedule for a teacher
    """

    day = models.CharField(
        "Día",
        max_length=10,
        choices=WeekDays.CHOICES,
        default=WeekDays.MONDAY,
        blank=False,
        null=False,
    )
    start_hour = models.TimeField("Hora de inicio", blank=False, null=False)
    end_hour = models.TimeField("Hora de finalización", blank=False, null=False)
    request_type = models.CharField(
        "Tipo de solicitud",
        max_length=10,
        choices=RequestType.CHOICES,
        default=RequestType.HOMEWORK,
        blank=False,
        null=False,
    )

    # Teacher field
    teacher = models.ForeignKey(
        Teacher,
        related_name="schedules",
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
