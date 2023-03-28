from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.requests.request_models.requestModels import Request


class Homework(SharedModelHistorical):
    """
    Model which represents a homework
    """

    COMPLETED = "COMPLETADO"
    PENDING = "PENDIENTE"
    NO_ANSWER = "SIN RESPUESTA"
    HOMEWORK_STATUS_CHOICES = (
        (COMPLETED, "Completado"),
        (PENDING, "Pendiente"),
        (NO_ANSWER, "Sin Respuesta"),
    )

    status = models.CharField(
        "Estado de la Tarea",
        max_length=20,
        choices=HOMEWORK_STATUS_CHOICES,
        default=PENDING,
        blank=False,
        null=False,
    )
    topic = models.CharField("Tema de la Tarea", max_length=100)
    details = models.TextField("Detalles de la Tarea", max_length=500)
    time_spent = models.IntegerField(
        "Tiempo invertido", default=0, blank=False, null=False
    )
    scheduled_date = models.DateField("Fecha programada", blank=False, null=False)
    request = models.OneToOneField(
        Request, on_delete=models.CASCADE, related_name="homework"
    )
