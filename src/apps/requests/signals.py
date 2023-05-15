import datetime

from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.shared.models.choices import RequestType, WeekDays
from apps.requests.models import Request
from apps.teachers.models import ScheduleSlot
from apps.homeworks.models import Homework
from apps.calendar.models import Event

from apps.calendar import create_calendar_event


def find_available_teacher_for_homework(request: Request) -> ScheduleSlot:
    """Finds an available teacher for the given request. It does so
    by finding an available schedule slot of a teacher that matches
    the subject of the request.

    Args:
        request (Request): the received request

    Returns:
        ScheduleSlot: the available schedule slot of a teacher
    """

    return ScheduleSlot.objects.filter(
        teacher__subjects=request.subject,
        request_type=RequestType.HOMEWORK,
        is_free=True,
    ).first()


def create_event_description(request: Request) -> str:
    """Creates the description of an event for the given request

    Args:
        request (Request): the received request

    Returns:
        str: the description of the event
    """

    description = (
        "El estudiante {} ha solicitado apoyo en TAREAS de la materia {}.\n".format(
            request.student.get_full_name(), request.subject.name
        )
    )

    if request.student.phone_number != None and request.student.phone_number != "":
        description += "Teléfono del estudiante: {}\n".format(
            request.student.phone_number
        )
    relatives = request.student.relatives.all()
    if relatives.exists():
        description += "Familiares del estudiante:\n"
        for relative in relatives:
            description += "Nombre: {} Teléfono: {}\n".format(
                relative.get_full_name(), relative.phone_number
            )

    return description


@receiver(post_save, sender=Request)
def handle_request_creation(sender, instance, created, **kwargs):
    """
    Handle what happens when a request is created
    """
    if created:
        available_slot = find_available_teacher_for_homework(instance)
        if not available_slot:
            return

        # mark the slot as not free
        available_slot.is_free = False
        available_slot.save()

        # find the date of the event according to the day of the week
        # of the available slot
        today = datetime.date.today()
        weekday = today.weekday()
        days_ahead = WeekDays.from_name_to_number(available_slot.day_of_week) - weekday
        if days_ahead <= 0:  # Target day already happened this week
            days_ahead += 7
        target_date = today + datetime.timedelta(days_ahead)
        start_time = datetime.datetime.combine(target_date, available_slot.start_time)
        end_time = datetime.datetime.combine(target_date, available_slot.end_time)

        # create a homework
        homework = Homework.objects.create(
            status=Homework.PENDING,
            topic="{} con el estudiante {}".format(
                instance.subject.name, instance.student.get_full_name()
            ),
            scheduled_date=target_date,
            request=instance,
        )

        # create an event
        event = Event.objects.create(
            summary="{} con el estudiante {}".format(
                instance.subject.name, instance.student.get_full_name()
            ),
            description=create_event_description(instance),
            start_time=start_time,
            end_time=end_time,
            homework=homework,
            schedule_slot=available_slot,
        )

        # assign the teacher to the request
        instance.teacher = available_slot.teacher
        instance.save()

        # create the calendar event
        create_calendar_event.delay(
            event.summary,
            event.description,
            event.start_time.isoformat(),
            event.end_time.isoformat(),
            [instance.teacher.user.email],
        )
