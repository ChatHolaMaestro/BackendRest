class RequestType:
    HOMEWORK = "TAREAS"
    ACADEMIC_REINFORCEMENT = "REFUERZO"
    ANY = "CUALQUIERA"

    CHOICES = (
        (HOMEWORK, "Apoyo en Tareas"),
        (ACADEMIC_REINFORCEMENT, "Refuerzo Académico"),
        (ANY, "Cualquiera"),
    )
