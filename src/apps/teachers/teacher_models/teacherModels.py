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
        
class Schedule(SharedModelHistorical):
    '''
    Model which represents a schedule for a teacher
    '''
    day = models.CharField(max_length=10, choices=WEEK_DAYS_CHOICES, blank=False, null=False)
    start_hour = models.TimeField(blank=False, null=False)
    end_hour = models.TimeField(blank=False, null=False)
    request_type = models.CharField(max_length=10, choices=REQUEST_TYPE_CHOICES, blank=False, null=False)
    
    #Teacher field
    teacher = models.ForeignKey(Teacher, related_name='schedules')
    
    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'