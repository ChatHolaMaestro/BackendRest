import datetime

from .service import (
    build_calendar_service,
    get_calendar_id,
    build_calendar_event,
    CalendarServiceException,
)
from config import celery_app


@celery_app.task
def create_calendar_event(
    summary: str,
    description: str,
    start: str,
    end: str,
    attendees: list[str],
):
    """Creates a calendar event calling the Google Calendar API.

    Args:
        summary (str): title of the event.
        description (str): short description of the event.
        start (str): start datetime of the event. Format: YYYY-MM-DDTHH:MM:SS
        end (str): end datetime of the event. Format: YYYY-MM-DDTHH:MM:SS
        attendees (list[str]): list of emails of the attendees.

    Raises:
        CalendarServiceException: If the event could not be created.
    """

    service = build_calendar_service()
    calendar_id = get_calendar_id()
    event = build_calendar_event(summary, description, start, end, attendees)

    try:
        event = (
            service.events()
            .insert(calendarId=calendar_id, body=event, sendUpdates="all")
            .execute()
        )
    except Exception as e:
        raise CalendarServiceException(f"Error creating event: {e}")


@celery_app.task
def clean_up_calendar_events():
    """Deletes all the events that have already passed from the database. Also
    updates their schedule slots to be free again and sets their homework / request
    status to completed.

    This should be a periodic task that runs every day at 00:00.
    """

    from apps.calendar.models import Event
    from apps.homeworks.models import Homework
    from apps.requests.models import Request

    events = Event.objects.filter(end_time__lt=datetime.datetime.now())
    for event in events:
        schedule_slot = event.schedule_slot
        schedule_slot.is_free = True
        schedule_slot.save()

        homework = event.homework
        homework.status = Homework.COMPLETED
        homework.save()

        request = homework.request
        request.status = Request.STATUS_COMPLETED
        request.save()

        event.delete()
