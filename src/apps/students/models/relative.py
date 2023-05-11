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
        if self is None:
            return ""
        return "{{id: {}, full_name: {}}}".format(str(self.id), self.get_full_name())
