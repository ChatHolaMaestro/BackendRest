import os.path

from django.conf import settings

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

from config import celery_app


class CalendarServiceException(Exception):
    pass


def build_calendar_service():
    """Builds a service object for interacting with the Calendar API.

    Returns:
        A service object for interacting with the Calendar API.

    Raises:
        CalendarServiceException: If the credentials are invalid.
    """

    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN):
        raise CalendarServiceException(
            "Could not find token.json file. Authenticate with `manage.py authgooglecalendar`"
        )

    try:
        creds = Credentials.from_authorized_user_file(
            settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, settings.GOOGLE_CALENDAR_SCOPES
        )
    except Exception as e:
        raise CalendarServiceException(f"Could not read credentials. Error: {e}")

    if creds.expired:
        try:
            creds.refresh(Request())
        except Exception as e:
            raise CalendarServiceException(f"Could not refresh credentials. Error: {e}")

        # Save the credentials for the next run
        with open(settings.GOOGLE_CALENDAR_PATH_TO_TOKEN, "w") as token:
            token.write(creds.to_json())

    return build("calendar", "v3", credentials=creds)


def get_calendar_id() -> str:
    """Get the calendar id from the file.

    Returns:
        The calendar id.

    Raises:
        CalendarServiceException: If the calendar id file does not exist.
    """
    if not os.path.exists(settings.GOOGLE_CALENDAR_PATH_TO_CALENDAR_ID):
        raise CalendarServiceException(
            "Could not find calendar id file. Select one with `manage.py selectgooglecalendar`"
        )

    with open(settings.GOOGLE_CALENDAR_PATH_TO_CALENDAR_ID, "r") as calendar_id_file:
        return calendar_id_file.read().strip()


def build_calendar_event(
    summary: str, description: str, start: str, end: str, attendees: list[str]
):
    return {
        "summary": summary,
        "description": description,
        "start": {
            "dateTime": start,
            "timeZone": "America/Bogota",
        },
        "end": {
            "dateTime": end,
            "timeZone": "America/Bogota",
        },
        "attendees": [{"email": attendee} for attendee in attendees],
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 30},
                {"method": "popup", "minutes": 10},
            ],
        },
    }


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
