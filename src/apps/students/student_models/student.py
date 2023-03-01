from django.db import models
from apps.shared.shared_models.GenericModels import SharedModelHistorical
from apps.shared.shared_models.IdentificationType import IDENTIFICATION_TYPES
from apps.students.student_models.studentChoices import STUDENT_GRADE, STUDENT_WORKING_HOURS
from apps.students.student_models.relative import Relative

from apps.schools.school_models.schoolModels import School

class Student(SharedModelHistorical):
    #Model which represents a student
    name = models.CharField('Nombre', max_length=100, blank=False)
    last_name = models.CharField('Apellido', max_length=100, blank=False)
    identification_type= models.CharField('Tipo de Identificación', max_length=3, choices=IDENTIFICATION_TYPES, default='TI', blank=False)
    identication_number = models.CharField('Número de Identificación', max_length=20, unique=True, blank=False)
    phone_number = models.CharField('Número de Teléfono', max_length=20)
    grade = models.CharField('Grado', max_length=3, choices=STUDENT_GRADE, blank=False)
    sex = models.CharField('Sexo', max_length=1, choices=[('M', 'Masculino'), ('F', 'Femenino')], blank=False)
    age = models.IntegerField('Edad')
    working_hours = models.CharField('Horario', max_length=1, choices=STUDENT_WORKING_HOURS, blank=False)
    #Many to many relationship with Relative
    relatives = models.ManyToManyField(Relative, related_name='students', blank=True)
    
    #Student's school
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students', blank=False)
        
    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"
        
    def __str__(self) -> str:
        return str(self.id)+' '+self.name + ' ' + self.last_name