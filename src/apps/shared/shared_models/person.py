from django.db import models
from django.core.validators import RegexValidator


class Person(models.Model):
    """
    Abstract model that represents a person's basic information.
    All other models that represent a person should inherit from this class.
    """
    
    IDENTIFICATION_TYPE_CHOICES = (
        ("TI", "Tarjeta de Identidad"),
        ("CC", "Cédula de Ciudadanía"),
        ("CE", "Cédula de Extranjería"),
        ("NUIP", "Número Único de Identificación Personal"),
        ("PA", "Pasaporte"),
    )

    first_name = models.CharField(
        "Nombre(s)", max_length=100, blank=True, help_text="Nombre de pila"
    )
    last_name = models.CharField(
        "Apellidos", max_length=100, blank=True, help_text="Apellidos completos"
    )
    identification_type = models.CharField(
        "Tipo de identificación",
        max_length=5,
        blank=True,
        null=True,
        choices=IDENTIFICATION_TYPE_CHOICES,
    )
    
    
    identification_number = models.CharField(
        "Número de identificación",
        max_length=20,
        blank=True,
        null=True,
        unique=True,
        help_text="Número de identificación sin puntos ni guiones",
        validators=[
            RegexValidator(
                regex=r"^\d+$",
                message="El número de identificación debe ser solo números sin puntos, guiones o espacios.",
                code="invalid_identification_number",
            )
        ],
    )
    phone_number = models.CharField(
        "Número de teléfono",
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^\d+$",
                message="El número de teléfono debe ser solo números sin puntos, guiones o espacios.",
                code="invalid_phone_number",
            )
        ],
    )

    def get_full_name(self) -> str:
        """Formats the full name of the user.

        Returns:
            str: first_name + last_name separated by a space.
        """
        full_name = "{} {}".format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self) -> str:
        """Returns the first name of the user.

        Returns:
            str: first_name
        """
        return self.first_name

    def get_formatted_identification(self) -> str:
        """Formats the identification number of the user. If the user has an
        identification type, it will be included in the format. Otherwise, only
        the identification number will be returned. If the user has no
        identification number, an empty string will be returned.

        Returns:
            str: identification_type + identification_number or
            identification_number or empty string.
        """
        if (
            self.identification_type is not None
            and self.identification_number is not None
        ):
            return "{} {}".format(
                self.get_identification_type_display(),
                self.identification_number,
            )
        elif self.identification_number is not None:
            return self.identification_number
        else:
            return ""

    class Meta:
        abstract = True
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
