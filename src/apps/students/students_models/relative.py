from apps.shared.models import SharedModelHistorical, Person


class Relative(SharedModelHistorical, Person):
    """
    Model which represents a relative. A relative is a person who is
    the guardian of a student.
    """

    class Meta:
        verbose_name = "Acudiente"
        verbose_name_plural = "Acudientes"

    def __str__(self) -> str:
        return "{} {}".format(str(self.id), self.get_full_name())
