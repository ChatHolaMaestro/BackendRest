from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.homeworks.models import Homework
from apps.teachers.models import ScheduleSlot


class Event(SharedModelHistorical):
    """
    Model that represents an event. An event is a Google Calendar event that is
    created when a teacher is available to attend a homework.
    """

    summary = models.CharField("Resumen", max_length=100)
    description = models.CharField("Descripción", max_length=500, blank=True)
    start_time = models.DateTimeField("Fecha de inicio")
    end_time = models.DateTimeField("Fecha de fin")
    homework = models.ForeignKey(
        Homework, on_delete=models.CASCADE, related_name="events"
    )
    schedule_slot = models.ForeignKey(
        ScheduleSlot, on_delete=models.CASCADE, related_name="events"
    )

    def __str__(self):
        return "{{summary: {}, start_time: {}, end_time: {}}}".format(
            str(self.summary), str(self.start_time), str(self.end_time)
        )
