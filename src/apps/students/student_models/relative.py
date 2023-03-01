from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical
from apps.shared.shared_models.shared_choices.IdentificationType import IDENTIFICATION_TYPES

class Relative(SharedModelHistorical):
    #Model which represents a relative
    name = models.CharField('Nombre', max_length=100)
    last_name = models.CharField('Apellido', max_length=100)
    identification_type= models.CharField('Tipo de Identificación', max_length=3, choices=IDENTIFICATION_TYPES, default='CC')
    identification_number = models.CharField('Número de Identificación', max_length=20, unique=True)
    phone_number = models.CharField('Número de Teléfono', max_length=20)
    
    class Meta:
        verbose_name = "Acudiente"
        verbose_name_plural = "Acudientes"
    
    def __str__(self) -> str:
        return str(self.id)+' '+self.name + ' ' + self.last_name