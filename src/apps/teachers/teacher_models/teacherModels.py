from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical
from apps.subjects.subject_models.subjectModels import Subject
from apps.shared.shared_models.shared_choices.WeekDays import WEEK_DAYS_CHOICES
from apps.shared.shared_models.shared_choices.RequestType import REQUEST_TYPE_CHOICES

class Teacher(SharedModelHistorical):
    '''
    Model which represents a teacher
    '''    
    #TODO add user field
    subjects = models.ManyToManyField(Subject, related_name='teachers')
    
    class Meta:
        verbose_name = 'Profesor'
        verbose_name_plural = 'Profesores'
        
    def __str__(self):
        #TODO return user name
        #return f'{self.user.first_name} {self.user.last_name}'
        return f'Profesor {self.id}'
        
class Schedule(SharedModelHistorical):
    '''
    Model which represents a schedule for a teacher
    '''
    day = models.CharField("Día", max_length=10, choices=WEEK_DAYS_CHOICES, blank=False, null=False)
    start_hour = models.TimeField("Hora de inicio", blank=False, null=False)
    end_hour = models.TimeField("Hora de finalización", blank=False, null=False)
    request_type = models.CharField("Tipo de solicitud", max_length=10, choices=REQUEST_TYPE_CHOICES, blank=False, null=False)
    
    #Teacher field
    teacher = models.ForeignKey(Teacher, related_name='schedules', on_delete=models.CASCADE, blank=False, null=False)
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'