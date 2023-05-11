from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.shared.models.choices import WeekDays, RequestType

from .teacher import Teacher


class ScheduleSlot(SharedModelHistorical):
    """
    Model that represents a schedule slot. A schedule slot is a time slot in which
    a teacher is available to attend requests. A teacher has many schedule slots.
    """

    day_of_week = models.CharField(
        "Día de la semana",
        max_length=10,
        choices=WeekDays.CHOICES,
        default=WeekDays.MONDAY,
        blank=False,
        null=False,
    )
    start_time = models.TimeField("Tiempo de inicio", blank=False, null=False)
    end_time = models.TimeField("Tiempo de finalización", blank=False, null=False)
    request_type = models.CharField(
        "Tipo de solicitud",
        max_length=10,
        choices=RequestType.CHOICES,
        default=RequestType.HOMEWORK,
        blank=False,
        null=False,
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        verbose_name="Profesor",
        related_name="schedule_slots",
    )

    class Meta:
        verbose_name = "Horario"
        verbose_name_plural = "Horarios"
