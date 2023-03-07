from django.db import models

from apps.shared.shared_models import SharedModelHistorical, Person
from apps.students.students_models import Relative
from apps.schools.school_models.schoolModels import School


class Student(SharedModelHistorical, Person):
    """
    Model which represents a student. The student is a person who is
    enrolled in a school and creates requests.
    """

    GRADE_CHOICES = [
        ("PJD", "Pre-Jardín"),
        ("JD", "Jardín"),
        ("TR", "Transición"),
        ("1", "Primero"),
        ("2", "Segundo"),
        ("3", "Tercero"),
        ("4", "Cuarto"),
        ("5", "Quinto"),
        ("6", "Sexto"),
        ("7", "Séptimo"),
        ("8", "Octavo"),
        ("9", "Noveno"),
        ("10", "Décimo"),
        ("11", "Once"),
    ]
    SEX_CHOICES = [("M", "Masculino"), ("F", "Femenino")]
    WORKING_HOURS_CHOICES = [("M", "Mañana"), ("T", "Tarde")]

    grade = models.CharField("Grado", max_length=3, choices=GRADE_CHOICES)
    sex = models.CharField("Sexo", max_length=1, choices=SEX_CHOICES, default="M")
    age = models.IntegerField("Edad")
    working_hours = models.CharField(
        "Jornada", max_length=1, choices=WORKING_HOURS_CHOICES, default="M"
    )

    # A student can have many relatives
    relatives = models.ManyToManyField(Relative, related_name="students", blank=True)
    # A student is enrolled in a school
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students", blank=False
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self) -> str:
        return "{} {}".format(str(self.id), self.get_full_name())
