from django.db import models
from apps.shared.shared_models import SharedModelHistorical
from apps.homeworks.homework_models.homeworkChoices import HOMEWORK_STATUS_CHOICES
from apps.requests.request_models.requestModels import Request


class Homework(SharedModelHistorical):
    """
    Model which represents a homework
    """

    status = models.CharField(
        "Estado de la Tarea",
        max_length=20,
        choices=HOMEWORK_STATUS_CHOICES,
        default="PENDIENTE",
        blank=False,
        null=False,
    )
    topic = models.CharField("Tema de la Tarea", max_length=100)
    details = models.TextField("Detalles de la Tarea", max_length=500)
    time_spent = models.IntegerField(
        "Tiempo invertido", default=0, blank=False, null=False
    )
    scheduled_date = models.DateField("Fecha programada", blank=False, null=False)
    # Foreign Keys
    request = models.OneToOneField(
        Request, on_delete=models.CASCADE, related_name="homework"
    )
