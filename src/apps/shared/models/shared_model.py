from django.db import models

from simple_history.models import HistoricalRecords


class SharedModel(models.Model):
    """
    Abstract model that contains the basic fields for all models
    """

    id = models.BigAutoField(primary_key=True)
    is_active = models.BooleanField("Estado", default=True)
    created_date = models.DateTimeField(
        "Fecha de creación", auto_now=False, auto_now_add=True
    )
    modified_date = models.DateTimeField(
        "Fecha de modificación", auto_now=True, auto_now_add=False
    )
    deleted_date = models.DateTimeField(
        "Fecha de eliminación", auto_now=True, auto_now_add=False, null=True, blank=True
    )

    class Meta:
        abstract = True
        verbose_name = "Modelo compartido"
        verbose_name_plural = "Modelos compartidos"


class SharedModelHistorical(SharedModel):
    """
    Abstract model that contains the basic fields for all models. This model also
    implements history tracking.
    """

    historical = HistoricalRecords(inherit=True)

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value

    class Meta:
        abstract = True
        verbose_name = "Modelo compartido con registro histórico"
        verbose_name_plural = "Modelos compartidos con registros históricos"
