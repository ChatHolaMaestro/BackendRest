from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.

#Shared model
class SharedModel(models.Model):
    
    id = models.AutoField(primary_key=True)
    is_active = models.BooleanField('Estado',default=True)
    created_date = models.DateTimeField('Fecha de creación',auto_now = False, auto_now_add=True)
    modified_date = models.DateTimeField('Fecha de modificación',auto_now = True, auto_now_add=False)
    deleted_date = models.DateTimeField('Fecha de eliminación',auto_now = True, auto_now_add=False, null=True, blank=True)

    class Meta:
        abstract = True
        verbose_name = "Modelo Compartido"
        verbose_name_plural = "Modelos Compartidos"
        

#Shared model with historical records Model
class SharedModelHistorical(SharedModel):
    historical = HistoricalRecords(inherit=True) 
    
    @property
    def _history_user(self):
        return self.changed_by
    
    @_history_user.setter
    def _history_user(self, value):
        self.changed_by = value
    
    class Meta:
        abstract = True
        verbose_name = "Modelo Compartido con Registro Histórico"
        verbose_name_plural = "Modelos Compartidos con Registros Históricos"