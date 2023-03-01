from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical

class School(SharedModelHistorical):
    '''
    Model which represents a school
    '''
    name = models.CharField("Nombre", max_length=100, unique=True)
    address = models.CharField("Dirección", max_length=150, blank = False)
    has_morning_hours = models.BooleanField("Jornada de mañana", default=True, blank = False)
    has_afternoon_hours = models.BooleanField("Jornada de tarde", default=False, blank = False)
    
class SchoolManager(SharedModelHistorical):
    '''
    Model which represents a school manager
    '''
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    #TODO: Add user field