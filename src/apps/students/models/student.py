from django.db import models

from apps.shared.models import SharedModelHistorical, Person
from apps.schools.models import School

from .relative import Relative


class Student(SharedModelHistorical, Person):
    """
    Model which represents a student. The student is a person who is
    enrolled in a school and creates requests.
    """

    GRADE_PJD = "PJD"
    GRADE_JD = "JD"
    GRADE_TR = "TR"
    GRADE_1 = "1"
    GRADE_2 = "2"
    GRADE_3 = "3"
    GRADE_4 = "4"
    GRADE_5 = "5"
    GRADE_6 = "6"
    GRADE_7 = "7"
    GRADE_8 = "8"
    GRADE_9 = "9"
    GRADE_10 = "10"
    GRADE_11 = "11"
    GRADE_CHOICES = (
        (GRADE_PJD, "Pre-Jardín"),
        (GRADE_JD, "Jardín"),
        (GRADE_TR, "Transición"),
        (GRADE_1, "1"),
        (GRADE_2, "2"),
        (GRADE_3, "3"),
        (GRADE_4, "4"),
        (GRADE_5, "5"),
        (GRADE_6, "6"),
        (GRADE_7, "7"),
        (GRADE_8, "8"),
        (GRADE_9, "9"),
        (GRADE_10, "10"),
        (GRADE_11, "11"),
    )

    SEX_MALE = "M"
    SEX_FEMALE = "F"
    SEX_CHOICES = (
        (SEX_MALE, "Masculino"),
        (SEX_FEMALE, "Femenino"),
    )

    WORKING_HOURS_MORNING = "M"
    WORKING_HOURS_AFTERNOON = "T"
    WORKING_HOURS_CHOICES = (
        (WORKING_HOURS_MORNING, "Mañana"),
        (WORKING_HOURS_AFTERNOON, "Tarde"),
    )

    grade = models.CharField("Grado", max_length=3, choices=GRADE_CHOICES)
    sex = models.CharField("Sexo", max_length=1, choices=SEX_CHOICES, default="M")
    age = models.IntegerField("Edad")
    working_hours = models.CharField(
        "Jornada", max_length=1, choices=WORKING_HOURS_CHOICES, default="M"
    )
    relatives = models.ManyToManyField(Relative, related_name="students", blank=True)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students", blank=False
    )

    class Meta:
        verbose_name = "Estudiante"
        verbose_name_plural = "Estudiantes"

    def __str__(self) -> str:
        if self is None:
            return ""
        return "{{id: {}, full_name: {}}}".format(str(self.id), self.get_full_name())
