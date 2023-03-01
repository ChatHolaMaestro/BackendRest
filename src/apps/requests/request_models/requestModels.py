from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical
from apps.requests.request_models.requestChoices import REQUEST_STATUS_CHOICES
from apps.shared.shared_models.shared_choices.RequestType import REQUEST_TYPE_CHOICES
from apps.students.student_models.student import Student
from apps.teachers.teacher_models.teacherModels import Teacher
from apps.subjects.subject_models.subjectModels import Subject

class Request(SharedModelHistorical):
    '''
    Model which represents a request
    '''
    
    status = models.CharField(max_length=20, choices=REQUEST_STATUS_CHOICES, default='CONTACTADO', null=False, blank=False)
    request_type = models.CharField(max_length=20, choices=REQUEST_TYPE_CHOICES, default='TAREAS' , null=False, blank=False)
    contact_times = models.IntegerField(default=0, null=False, blank=False)
    
    # Foreign Keys
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=False, blank=False)
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, null=False, blank=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, null=False, blank=False)
    
    class Meta:
        verbose_name = 'Solicitud'
        verbose_name_plural = 'Solicitudes'