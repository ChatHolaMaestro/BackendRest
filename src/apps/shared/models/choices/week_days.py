class WeekDays:
    MONDAY = "LUNES"
    TUESDAY = "MARTES"
    WEDNESDAY = "MIERCOLES"
    THURSDAY = "JUEVES"
    FRIDAY = "VIERNES"
    SATURDAY = "SABADO"
    SUNDAY = "DOMINGO"

    CHOICES = (
        (MONDAY, "Lunes"),
        (TUESDAY, "Martes"),
        (WEDNESDAY, "Miércoles"),
        (THURSDAY, "Jueves"),
        (FRIDAY, "Viernes"),
        (SATURDAY, "Sábado"),
        (SUNDAY, "Domingo"),
    )

    @classmethod
    def from_name_to_number(cls, name):
        for pos, choice in enumerate(cls.CHOICES):
            if choice[0] == name:
                return pos
        return None
