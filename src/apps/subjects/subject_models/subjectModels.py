from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical

class Subject(SharedModelHistorical):
    #Model which represents a subject
    name = models.CharField('Nombre', max_length=100, blank=False)
    
    class Meta:
        verbose_name = "Asignatura"
        verbose_name_plural = "Asignaturas"
        
    def __str__(self) -> str:
        return str(self.id)+' '+self.name