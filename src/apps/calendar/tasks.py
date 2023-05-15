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
