from django.db import models

from apps.shared.models import SharedModelHistorical
from apps.shared.models.choices import RequestType
from apps.students.models import Student
from apps.teachers.models import Teacher
from apps.subjects.models import Subject


class Request(SharedModelHistorical):
    """
    Model which represents a request
    """

    STATUS_PENDING = "PENDIENTE"
    STATUS_COMPLETED = "COMPLETADO"
    STATUS_CONTACTED = "CONTACTADO"
    STATUS_CANCELLED = "CANCELADO"
    REQUEST_STATUS_CHOICES = (
        (STATUS_PENDING, "Pendiente"),
        (STATUS_COMPLETED, "Completado"),
        (STATUS_CONTACTED, "Contactado"),
        (STATUS_CANCELLED, "Cancelado"),
    )

    status = models.CharField(
        max_length=20,
        choices=REQUEST_STATUS_CHOICES,
        default=STATUS_CONTACTED,
        null=False,
        blank=False,
    )
    request_type = models.CharField(
        max_length=20,
        choices=RequestType.CHOICES,
        default=RequestType.HOMEWORK,
        null=False,
        blank=False,
    )
    contact_times = models.IntegerField(default=0, null=False, blank=False)

    # Foreign Keys
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, null=False, blank=False
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, null=True, blank=False
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=False, blank=False
    )

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"

    def __str__(self):
        return "{{id: {}, student: {}, teacher: {}, subject: {}}}".format(
            str(self.id), str(self.student), str(self.teacher), str(self.subject)
        )
