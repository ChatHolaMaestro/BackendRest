from django.db import models

from apps.shared.models import SharedModelHistorical


class Subject(SharedModelHistorical):
    """
    Model that represents a subject. Teachers have many subjects.
    """

    name = models.CharField("Nombre", max_length=100, blank=False)

    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"

    def __str__(self) -> str:
        return "{{id: {}, name: {}}}".format(self.id, self.name)
